from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from functools import wraps
import json

from .models import (
    Cliente, Proveedor, Tecnico, Administrador, Marca, 
    Producto, Equipo, OrdenServicio, ServicioTecnico, 
    Ventas, ComprasMercancia, Garantias, Facturacion,
    UserProfile, Category, Product, Cart, CartItem, Order, OrderItem, Invoice
)
from .forms import (
    CustomUserCreationForm, CustomAuthenticationForm, 
    ForgotPasswordForm, CustomPasswordResetForm, ContactForm,
    RoleSelectionForm, ClienteRegistrationForm, 
    ProveedorRegistrationForm, AdministradorRegistrationForm
)
from django.http import HttpResponseRedirect

def superuser_required(view_func):
    """Decorador que requiere que el usuario sea superusuario"""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('main:login')
        if not request.user.is_superuser:
            messages.error(request, 'No tienes permisos para acceder a esta sección.')
            return redirect('main:home')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def role_required(*allowed_roles):
    """Decorador que requiere que el usuario tenga uno de los roles especificados"""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('main:login')
            
            # Verificar si el usuario tiene perfil
            if hasattr(request.user, 'profile'):
                user_role = request.user.profile.role
                if user_role in allowed_roles or request.user.is_superuser:
                    return view_func(request, *args, **kwargs)
            
            messages.error(request, 'No tienes permisos para acceder a esta sección.')
            return redirect('main:home')
        return _wrapped_view
    return decorator


def admin_or_role_required(*allowed_roles):
    """Decorador que permite acceso a administradores o usuarios con roles específicos"""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('main:login')
            
            # Los superusuarios siempre tienen acceso
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
                
            # Verificar si el usuario tiene perfil y el rol adecuado
            if hasattr(request.user, 'profile'):
                user_role = request.user.profile.role
                if user_role == 'administrador' or user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            
            messages.error(request, 'No tienes permisos para acceder a esta sección.')
            return redirect('main:home')
        return _wrapped_view
    return decorator

def home(request):
    """Vista principal del sitio web - para todos los usuarios autenticados"""
    if not request.user.is_authenticated:
        # Redireccionar a página de bienvenida para usuarios no autenticados
        return redirect('main:welcome')
    
    context = {
        'title': 'Digit Soft - Soluciones Informáticas',
        'company_name': 'Digit Soft',
        'company_slogan': 'Soluciones Tecnológicas',
        'user': request.user,
    }
    return render(request, 'main/home.html', context)


def welcome(request):
    """Página de bienvenida para usuarios no autenticados"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    context = {
        'title': 'Bienvenido a Digit Soft',
        'company_name': 'Digit Soft',
        'company_slogan': 'Soluciones Tecnológicas',
    }
    return render(request, 'main/welcome.html', context)


# =============================================
# VISTAS DE AUTENTICACIÓN
# =============================================

def login_view(request):
    """Vista para iniciar sesión"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Configurar duración de sesión
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 semanas
                else:
                    request.session.set_expiry(0)  # Se cierra al cerrar navegador
                
                messages.success(request, f'¡Bienvenido de nuevo, {user.first_name}!')
                
                # Redireccionar a la página solicitada o home
                next_page = request.GET.get('next', 'main:home')
                return redirect(next_page)
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomAuthenticationForm()
    
    context = {
        'form': form,
        'title': 'Iniciar Sesión - Digit Soft'
    }
    return render(request, 'main/auth/login.html', context)


def register_view(request):
    """Vista para seleccionar tipo de registro"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            return redirect('main:register_user', role=role)
    else:
        form = RoleSelectionForm()
    
    context = {
        'form': form,
        'title': 'Seleccionar Tipo de Cuenta - Digit Soft'
    }
    return render(request, 'main/auth/register_role_selection.html', context)


def register_user_view(request, role):
    """Vista para registrar usuario según el rol seleccionado"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    # Validar que el rol sea válido
    valid_roles = ['cliente', 'proveedor', 'administrador']
    if role not in valid_roles:
        messages.error(request, 'Tipo de cuenta no válido.')
        return redirect('main:register')
    
    # Seleccionar el formulario según el rol
    form_classes = {
        'cliente': ClienteRegistrationForm,
        'proveedor': ProveedorRegistrationForm,
        'administrador': AdministradorRegistrationForm,
    }
    
    FormClass = form_classes[role]
    
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                role_names = {
                    'cliente': 'Cliente',
                    'proveedor': 'Proveedor', 
                    'administrador': 'Administrador'
                }
                
                messages.success(
                    request, 
                    f'¡Cuenta de {role_names[role]} creada exitosamente! Bienvenido, {user.first_name}.'
                )
                
                # Autenticar y loguear automáticamente
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    return redirect('main:home')
                else:
                    return redirect('main:login')
                    
            except Exception as e:
                messages.error(request, 'Ocurrió un error al crear la cuenta. Intenta nuevamente.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = FormClass()
    
    role_names = {
        'cliente': 'Cliente',
        'proveedor': 'Proveedor',
        'administrador': 'Administrador'
    }
    
    context = {
        'form': form,
        'role': role,
        'role_name': role_names[role],
        'title': f'Registro de {role_names[role]} - Digit Soft'
    }
    return render(request, 'main/auth/register_user.html', context)


def forgot_password_view(request):
    """Vista para recuperar contraseña"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            try:
                user = User.objects.get(email=email)
                
                # Generar token para reset
                reset_token = get_random_string(32)
                
                # Crear URL de reset
                reset_url = request.build_absolute_uri(
                    reverse('main:reset_password') + f'?token={reset_token}&email={email}'
                )
                
                # Simular envío de email (en producción usar send_mail)
                print(f"\n=== EMAIL DE RECUPERACIÓN ===")
                print(f"Para: {email}")
                print(f"Enlace de recuperación: {reset_url}")
                print(f"Token: {reset_token}")
                print(f"================================\n")
                
                messages.success(request, 'Se ha enviado un enlace de recuperación a tu correo electrónico.')
                
            except User.DoesNotExist:
                # Por seguridad, no revelar si el email existe o no
                messages.success(request, 'Si el correo existe, recibirás un enlace de recuperación.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ForgotPasswordForm()
    
    context = {
        'form': form,
        'title': 'Recuperar Contraseña - Digit Soft'
    }
    return render(request, 'main/auth/forgot_password.html', context)


def reset_password_view(request):
    """Vista para establecer nueva contraseña"""
    if request.user.is_authenticated:
        return redirect('main:home')
    
    token = request.GET.get('token')
    email = request.GET.get('email')
    
    if not token or not email:
        messages.error(request, 'Enlace de recuperación inválido.')
        return redirect('main:forgot_password')
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('main:forgot_password')
    
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['password1']
            user.set_password(new_password)
            user.save()
            
            messages.success(request, '¡Contraseña actualizada exitosamente! Ya puedes iniciar sesión.')
            return redirect('main:login')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomPasswordResetForm()
    
    context = {
        'form': form,
        'title': 'Restablecer Contraseña - Digit Soft',
        'token': token,
        'email': email
    }
    return render(request, 'main/auth/reset_password.html', context)


@login_required
def logout_view(request):
    """Vista para cerrar sesión"""
    user_name = request.user.first_name or request.user.username
    logout(request)
    messages.success(request, f'¡Hasta luego, {user_name}! Has cerrado sesión exitosamente.')
    return redirect('main:home')


@login_required
def profile_view(request):
    """Vista del perfil de usuario mejorada"""
    user = request.user
    
    # Verificar si el usuario tiene perfil
    has_profile = hasattr(user, 'profile') and user.profile
    
    context = {
        'user': user,
        'has_profile': has_profile,
        'title': f'Perfil de {user.first_name or user.username} - Digit Soft'
    }
    
    # Si tiene perfil, agregar información adicional
    if has_profile:
        profile = user.profile
        context.update({
            'profile': profile,
            'role_display': profile.get_role_display(),
            'is_cliente': profile.is_cliente,
            'is_administrador': profile.is_administrador,
            'is_proveedor': profile.is_proveedor,
            'is_tecnico': profile.is_tecnico,
        })
    
    return render(request, 'main/auth/profile.html', context)


@login_required
def admin_panel_view(request):
    """Vista del panel de administración - solo para staff y superusers"""
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, 'No tienes permisos para acceder al panel de administración.')
        return redirect('main:home')
    
    # Estadísticas básicas
    from django.contrib.auth.models import User
    from .models import UserProfile
    
    context = {
        'title': 'Panel de Administración - Digit Soft',
        'total_users': User.objects.count(),
        'total_profiles': UserProfile.objects.count(),
        'total_clientes': UserProfile.objects.filter(role='cliente').count(),
        'total_administradores': UserProfile.objects.filter(role='administrador').count(),
        'total_proveedores': UserProfile.objects.filter(role='proveedor').count(),
        'total_tecnicos': UserProfile.objects.filter(role='técnico').count(),
        'recent_users': User.objects.order_by('-date_joined')[:10],
    }
    
    return render(request, 'main/admin/admin_panel.html', context)


@login_required
def history_view(request):
    """Vista del historial de usuario"""
    user = request.user
    
    # Por ahora, mostraremos un historial básico
    # En el futuro se puede expandir con pedidos, compras, etc.
    context = {
        'title': f'Historial de {user.first_name or user.username} - Digit Soft',
        'user': user,
        'has_profile': hasattr(user, 'profile') and user.profile,
    }
    
    # Si tiene perfil, agregar información adicional
    if hasattr(user, 'profile') and user.profile:
        context['profile'] = user.profile
    
    return render(request, 'main/auth/history.html', context)


def test_carrito_view(request):
    """Vista de prueba para el carrito"""
    return render(request, 'main/test_carrito.html', {
        'title': 'Prueba del Carrito - Digit Soft'
    })


def contact_view(request):
    """Vista mejorada para formulario de contacto"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar formulario de contacto
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', '')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Aquí normalmente enviarías el email o guardarías en BD
            print(f"\n=== NUEVO MENSAJE DE CONTACTO ===")
            print(f"Nombre: {name}")
            print(f"Email: {email}")
            print(f"Teléfono: {phone}")
            print(f"Tema: {subject}")
            print(f"Mensaje: {message}")
            print(f"================================\n")
            
            messages.success(request, '¡Mensaje enviado exitosamente! Te contactaremos pronto.')
            return redirect('main:home')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'title': 'Contacto - Digit Soft'
    }
    return render(request, 'main/contact.html', context)

def servicios(request):
    """Vista de servicios"""
    servicios_list = [
        {
            'titulo': 'Infraestructura',
            'descripcion': 'Hosting - Dominio, Correo Corporativo, Configuración de servidores, Cableado Estructurado.',
            'icono': 'fas fa-tools'
        },
        {
            'titulo': 'Soporte Técnico',
            'descripcion': 'CCTV y Cámaras, Presencial y Remoto, Backups y Respaldos de Información, Mantenimiento Preventivo y Correctivo de equipos de Cómputo.',
            'icono': 'fas fa-wrench'
        },
        {
            'titulo': 'Software',
            'descripcion': 'Desarrollo a la Medida, Servicios Cloud, Data Analytics, Business Intelligence (BI).',
            'icono': 'fas fa-shield-alt'
        },
        {
            'titulo': 'Diseño Web',
            'descripcion': 'Landing Page - Blogs, Sitios Web Informativos y Corporativos, Tiendas Online, Posicionamiento SEO y SEM.',
            'icono': 'fas fa-network-wired'
        },
        {
            'titulo': 'Venta',
            'descripcion': 'PC y Portátiles-Equipos Corporativos, Impresoras - Cámaras de Seguridad, Accesorios PC - Retail y POS, UPS - Biométricos - Licenciamiento.',
            'icono': 'fas fa-cloud'
        },
        {
            'titulo': 'Soporte Remoto',
            'descripcion': 'Asistencia técnica inmediata sin necesidad de desplazamiento.',
            'icono': 'fas fa-headset'
        }
    ]
    
    context = {
        'title': 'Nuestros Servicios - Digit Soft',
        'servicios': servicios_list,
    }
    return render(request, 'main/servicios.html', context)

@csrf_exempt
def contact_form(request):
    """Procesar formulario de contacto"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Aquí puedes procesar el formulario
            # Por ejemplo, enviar email, guardar en base de datos, etc.
            
            response_data = {
                'success': True,
                'message': f'Gracias {data.get("name", "")}, hemos recibido tu mensaje y nos pondremos en contacto pronto.'
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'Error al procesar el formulario. Por favor, inténtalo de nuevo.'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido.'})

@csrf_exempt
def login_form(request):
    """Procesar formulario de login"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            role = data.get('role', 'client')
            
            # Aquí implementarías la lógica de autenticación
            # Por ahora, solo simulamos una respuesta exitosa
            
            role_names = {
                'admin': 'Administrador',
                'technician': 'Técnico',
                'client': 'Cliente'
            }
            
            response_data = {
                'success': True,
                'message': f'Bienvenido {email} ({role_names.get(role, "Cliente")})',
                'redirect_url': '/'  # Aquí puedes redirigir según el rol
            }
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'Error al procesar el login. Por favor, inténtalo de nuevo.'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido.'})


# Vistas de Gestión de Módulos

@superuser_required
def gestion_clientes(request):
    """Vista para gestión de clientes con datos relacionados"""
    clientes = Cliente.objects.all().order_by('-fecha_creacion')
    
    # Obtener datos relacionados para cada cliente
    clientes_data = []
    for cliente in clientes:
        ordenes = OrdenServicio.objects.filter(cliente=cliente)
        ventas = Ventas.objects.filter(cliente=cliente)
        servicios = ServicioTecnico.objects.filter(cliente=cliente)
        
        clientes_data.append({
            'cliente': cliente,
            'ordenes_count': ordenes.count(),
            'ventas_count': ventas.count(),
            'servicios_count': servicios.count(),
            'ordenes': ordenes[:3],  # Últimas 3 órdenes
            'ventas': ventas[:3],    # Últimas 3 ventas
        })
    
    # Paginación
    paginator = Paginator(clientes_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'clientes_data': page_obj,
        'total_clientes': clientes.count(),
        'title': 'Gestión de Clientes'
    }
    return render(request, 'main/gestion_clientes.html', context)

@superuser_required
def gestion_productos(request):
    """Vista para gestión de productos con datos relacionados - solo administrador"""
    productos = Producto.objects.select_related('marca').all().order_by('nombreProducto')
    
    # Obtener datos relacionados para cada producto
    productos_data = []
    for producto in productos:
        compras = ComprasMercancia.objects.filter(producto=producto)
        ventas = Ventas.objects.filter(producto=producto)
        
        productos_data.append({
            'producto': producto,
            'compras_count': compras.count(),
            'ventas_count': ventas.count(),
            'stock_actual': producto.cantidad,
            'compras': compras[:3],  # Últimas 3 compras
            'ventas': ventas[:3],    # Últimas 3 ventas
        })
    
    # Paginación
    paginator = Paginator(productos_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Obtener marcas para filtros
    marcas = Marca.objects.all()
    
    context = {
        'productos_data': page_obj,
        'marcas': marcas,
        'total_productos': productos.count(),
        'title': 'Gestión de Productos'
    }
    return render(request, 'main/gestion_productos.html', context)

def gestion_proveedores(request):
    """Vista para gestión de proveedores con datos relacionados"""
    proveedores = Proveedor.objects.all().order_by('nombre')
    
    # Obtener datos relacionados para cada proveedor
    proveedores_data = []
    for proveedor in proveedores:
        compras = ComprasMercancia.objects.filter(proveedor=proveedor)
        productos_suministrados = compras.values('producto').distinct().count()
        
        proveedores_data.append({
            'proveedor': proveedor,
            'compras_count': compras.count(),
            'productos_count': productos_suministrados,
            'compras': compras[:5],  # Últimas 5 compras
        })
    
    # Paginación
    paginator = Paginator(proveedores_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'proveedores_data': page_obj,
        'total_proveedores': proveedores.count(),
        'title': 'Gestión de Proveedores'
    }
    return render(request, 'main/gestion_proveedores.html', context)

def gestion_compras(request):
    """Vista para gestión de compras con datos relacionados"""
    compras = ComprasMercancia.objects.select_related(
        'producto', 'proveedor', 'administrador'
    ).all().order_by('-fecha_creacion')
    
    # Paginación
    paginator = Paginator(compras, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Estadísticas
    total_compras = compras.count()
    productos_comprados = compras.values('producto').distinct().count()
    proveedores_activos = compras.values('proveedor').distinct().count()
    
    context = {
        'compras': page_obj,
        'total_compras': total_compras,
        'productos_comprados': productos_comprados,
        'proveedores_activos': proveedores_activos,
        'title': 'Gestión de Compras'
    }
    return render(request, 'main/gestion_compras.html', context)

def orden_servicio(request):
    """Vista para gestión de órdenes de servicio"""
    ordenes = OrdenServicio.objects.select_related(
        'cliente', 'tecnico'
    ).all().order_by('-fecha_creacion')
    
    # Obtener datos relacionados
    ordenes_data = []
    for orden in ordenes:
        servicios = ServicioTecnico.objects.filter(orden_servicio=orden)
        facturas = Facturacion.objects.filter(orden_servicio=orden)
        
        ordenes_data.append({
            'orden': orden,
            'servicios_count': servicios.count(),
            'facturas_count': facturas.count(),
            'servicios': servicios,
            'facturas': facturas[:2],  # Últimas 2 facturas
        })
    
    # Paginación
    paginator = Paginator(ordenes_data, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Estadísticas
    total_ordenes = ordenes.count()
    ordenes_pendientes = ordenes.filter(estado='Pendiente').count()
    ordenes_completadas = ordenes.filter(estado='Completada').count()
    
    context = {
        'ordenes_data': page_obj,
        'total_ordenes': total_ordenes,
        'ordenes_pendientes': ordenes_pendientes,
        'ordenes_completadas': ordenes_completadas,
        'title': 'Órdenes de Servicio'
    }
    return render(request, 'main/orden_servicio.html', context)

@superuser_required
def gestion_ventas(request):
    """Vista para gestión de ventas - solo administrador"""
    ventas = Ventas.objects.select_related(
        'cliente', 'producto'
    ).all().order_by('-fecha_venta')
    
    # Paginación
    paginator = Paginator(ventas, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Estadísticas
    total_ventas = ventas.count()
    productos_vendidos = sum(venta.cantidad_vendidas for venta in ventas)
    clientes_unicos = ventas.values('cliente').distinct().count()
    
    context = {
        'ventas': page_obj,
        'total_ventas': total_ventas,
        'productos_vendidos': productos_vendidos,
        'clientes_unicos': clientes_unicos,
        'title': 'Gestión de Ventas'
    }
    return render(request, 'main/gestion_ventas.html', context)

def gestion_tecnicos(request):
    """Vista para gestión de técnicos"""
    tecnicos = Tecnico.objects.all().order_by('nombre_completo')
    
    # Obtener datos relacionados para cada técnico
    tecnicos_data = []
    for tecnico in tecnicos:
        ordenes = OrdenServicio.objects.filter(tecnico=tecnico)
        servicios = ServicioTecnico.objects.filter(tecnico=tecnico)
        
        tecnicos_data.append({
            'tecnico': tecnico,
            'ordenes_count': ordenes.count(),
            'servicios_count': servicios.count(),
            'ordenes_activas': ordenes.filter(estado='Pendiente').count(),
            'ordenes': ordenes[:3],  # Últimas 3 órdenes
        })
    
    # Paginación
    paginator = Paginator(tecnicos_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'tecnicos_data': page_obj,
        'total_tecnicos': tecnicos.count(),
        'title': 'Gestión de Técnicos'
    }
    return render(request, 'main/gestion_tecnicos.html', context)

def servicio_tecnico(request):
    """Vista para servicios técnicos"""
    servicios = ServicioTecnico.objects.select_related(
        'cliente', 'tecnico', 'orden_servicio'
    ).all().order_by('-id_servicio_tecnico')
    
    # Paginación
    paginator = Paginator(servicios, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'servicios': page_obj,
        'total_servicios': servicios.count(),
        'title': 'Servicio Técnico'
    }
    return render(request, 'main/servicio_tecnico.html', context)

def gestion_garantias(request):
    """Vista para gestión de garantías"""
    garantias = Garantias.objects.all().order_by('-id_garantias')
    
    # Paginación
    paginator = Paginator(garantias, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'garantias': page_obj,
        'total_garantias': garantias.count(),
        'title': 'Gestión de Garantías'
    }
    return render(request, 'main/gestion_garantias.html', context)

@login_required
def admin_panel(request):
    """Panel de administración - solo para superusuarios"""
    # Verificar que sea superusuario
    if not request.user.is_superuser:
        messages.error(request, 'No tienes permisos para acceder al panel de administración.')
        return redirect('main:home')
    
    # Estadísticas generales del sistema
    stats = {
        'total_clientes': Cliente.objects.count(),
        'total_productos': Producto.objects.count(),
        'total_ordenes': OrdenServicio.objects.count(),
        'total_ventas': Ventas.objects.count(),
        'ordenes_pendientes': OrdenServicio.objects.filter(estado='Pendiente').count(),
        'productos_bajo_stock': Producto.objects.filter(cantidad__lt=10).count(),
    }
    
    # Actividad reciente
    ordenes_recientes = OrdenServicio.objects.select_related('cliente', 'tecnico').order_by('-fecha_creacion')[:5]
    ventas_recientes = Ventas.objects.select_related('cliente', 'producto').order_by('-fecha_venta')[:5]
    
    context = {
        'stats': stats,
        'ordenes_recientes': ordenes_recientes,
        'ventas_recientes': ventas_recientes,
        'title': 'Panel de Administración'
    }
    return render(request, 'main/admin_panel.html', context)

def carrito(request):
    """Vista del carrito de compras"""
    context = {
        'title': 'Carrito de Compras - Digit Soft'
    }
    return render(request, 'main/carrito/carrito.html', context)


# ==========================================
# VISTAS DE OAUTH SOCIAL LOGIN
# ==========================================

def google_oauth_login(request):
    """Vista para login con Google"""
    # URL de OAuth de Google
    google_oauth_url = (
        "https://accounts.google.com/oauth/authorize"
        "?client_id=YOUR_GOOGLE_CLIENT_ID"
        "&redirect_uri=http://127.0.0.1:8000/auth/google/callback/"
        "&scope=openid email profile"
        "&response_type=code"
        "&access_type=online"
    )
    
    # Por ahora, mostrar un mensaje informativo
    messages.info(
        request, 
        "Funcionalidad de Google OAuth en desarrollo. "
        "Para usar esta función, configura las credenciales de Google OAuth en el panel de administración."
    )
    return redirect('main:login')

def microsoft_oauth_login(request):
    """Vista para login con Microsoft"""
    # URL de OAuth de Microsoft
    microsoft_oauth_url = (
        "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
        "?client_id=YOUR_MICROSOFT_CLIENT_ID"
        "&response_type=code"
        "&redirect_uri=http://127.0.0.1:8000/auth/microsoft/callback/"
        "&scope=openid email profile"
    )
    
    # Por ahora, mostrar un mensaje informativo
    messages.info(
        request, 
        "Funcionalidad de Microsoft OAuth en desarrollo. "
        "Para usar esta función, configura las credenciales de Microsoft OAuth en el panel de administración."
    )
    return redirect('main:login')

def google_oauth_callback(request):
    """Callback para OAuth de Google"""
    # Aquí procesarías el código de autorización de Google
    messages.success(request, "Login con Google procesado correctamente!")
    return redirect('main:home')

def microsoft_oauth_callback(request):
    """Callback para OAuth de Microsoft"""
    # Aquí procesarías el código de autorización de Microsoft
    messages.success(request, "Login con Microsoft procesado correctamente!")
    return redirect('main:home')


# =============================================
# VISTAS DE PRODUCTOS Y E-COMMERCE
# =============================================

def products_view(request):
    """Vista principal del catálogo de productos"""
    category_param = request.GET.get('category')
    search_query = request.GET.get('search', '')
    
    products = Product.objects.filter(is_active=True)
    
    # Filtrar por categoría si se especifica
    if category_param:
        products = products.filter(category__name=category_param)
    
    # Filtrar por búsqueda si se especifica
    if search_query:
        products = products.filter(
            name__icontains=search_query
        ).distinct()
    
    # Obtener todas las categorías para el menú
    categories = Category.objects.all().order_by('name')
    
    # Paginación
    paginator = Paginator(products, 12)  # 12 productos por página
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'title': 'Catálogo de Productos - Digit Soft',
        'products': products,
        'categories': categories,
        'current_category': category_param,
        'search_query': search_query,
    }
    return render(request, 'main/products/catalog.html', context)


def category_products_view(request, category_slug):
    """Vista para mostrar productos de una categoría específica"""
    category = get_object_or_404(Category, name=category_slug)
    products = Product.objects.filter(category=category, is_active=True)
    
    # Filtrar por búsqueda si se especifica
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    # Paginación
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    # Obtener todas las categorías para el menú
    categories = Category.objects.all().order_by('name')
    
    context = {
        'title': f'{category.name} - Digit Soft',
        'products': products,
        'categories': categories,
        'current_category': category,
        'search_query': search_query,
    }
    return render(request, 'main/products/category.html', context)


def product_detail_view(request, product_id):
    """Vista detallada de un producto específico"""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    
    # Productos relacionados de la misma categoría
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(pk=product.pk)[:4]
    
    context = {
        'title': f'{product.name} - Digit Soft',
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'main/products/detail.html', context)


@csrf_exempt
def add_to_cart_view(request):
    """Vista AJAX para añadir productos al carrito"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            quantity = int(data.get('quantity', 1))
            
            product = get_object_or_404(Product, id=product_id, is_active=True)
            
            if request.user.is_authenticated:
                # Usuario autenticado - usar carrito en base de datos
                cart, created = Cart.objects.get_or_create(
                    user=request.user,
                    defaults={'created_at': timezone.now()}
                )
                
                cart_item, item_created = CartItem.objects.get_or_create(
                    cart=cart,
                    product=product,
                    defaults={'quantity': quantity}
                )
                
                if not item_created:
                    cart_item.quantity += quantity
                    cart_item.save()
                
                # Calcular totales del carrito
                total_items = cart.cartcartitem__setet.count()
                total_amount = sum(
                    item.product.price * item.quantity 
                    for item in cart.cartcartitem__setet.all()
                )
                
            else:
                # Usuario no autenticado - usar sesión
                cart = request.session.get('cart', {})
                
                if str(product_id) in cart:
                    cart[str(product_id)] += quantity
                else:
                    cart[str(product_id)] = quantity
                
                request.session['cart'] = cart
                request.session.modified = True
                
                # Calcular totales para sesión
                total_items = len(cart)
                total_amount = sum(
                    Product.objects.get(id=pid).price * qty
                    for pid, qty in cart.items()
                )
            
            return JsonResponse({
                'success': True,
                'message': f'{product.name} añadido al carrito',
                'cart_count': total_items,
                'cart_total': float(total_amount)
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error al añadir al carrito: {str(e)}'
            }, status=400)
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)


@csrf_exempt
def remove_from_cart_view(request):
    """Vista AJAX para eliminar productos del carrito"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            
            if request.user.is_authenticated:
                cart = Cart.objects.get(user=request.user)
                CartItem.objects.filter(cart=cart, product_id=product_id).delete()
                
                # Recalcular totales
                total_items = cart.items.count()
                total_amount = sum(
                    item.product.price * item.quantity 
                    for item in cart.items.all()
                )
                
            else:
                cart = request.session.get('cart', {})
                if str(product_id) in cart:
                    del cart[str(product_id)]
                    request.session['cart'] = cart
                    request.session.modified = True
                
                total_items = len(cart)
                total_amount = sum(
                    Product.objects.get(id=pid).price * qty
                    for pid, qty in cart.items()
                )
            
            return JsonResponse({
                'success': True,
                'message': 'Producto eliminado del carrito',
                'cart_count': total_items,
                'cart_total': float(total_amount)
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error al eliminar del carrito: {str(e)}'
            }, status=400)
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)


def cart_view(request):
    """Vista del carrito de compras"""
    cart_items = []
    total_amount = 0
    
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = cart.cartitem_set.all()
            total_amount = sum(
                item.product.price * item.quantity 
                for item in cart_items
            )
        except Cart.DoesNotExist:
            pass
    else:
        cart = request.session.get('cart', {})
        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'subtotal': product.price * quantity
                })
                total_amount += product.price * quantity
            except Product.DoesNotExist:
                continue
    
    context = {
        'title': 'Carrito de Compras - Digit Soft',
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'main/cart/cart.html', context)


@login_required
def checkout_view(request):
    """Vista para procesar el checkout"""
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        
        if not cart_items.exists():
            messages.error(request, 'Tu carrito está vacío.')
            return redirect('main:cart')
        
        if request.method == 'POST':
            # Crear orden
            total_amount = sum(
                item.product.price * item.quantity 
                for item in cart_items
            )
            
            order = Order.objects.create(
                user=request.user,
                total_amount=total_amount,
                status='pending'
            )
            
            # Crear items de la orden
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
            
            # Crear factura
            invoice = Invoice.objects.create(
                order=order
            )
            
            # Limpiar carrito
            cart_items.delete()
            
            messages.success(request, f'¡Pedido realizado exitosamente! Número de factura: {invoice.invoice_number}')
            return redirect('main:invoice_detail', invoice_id=invoice.pk)
        
        # Calcular total
        total_amount = sum(
            item.product.price * item.quantity 
            for item in cart_items
        )
        
        context = {
            'title': 'Finalizar Compra - Digit Soft',
            'cart_items': cart_items,
            'total_amount': total_amount,
        }
        return render(request, 'main/cart/checkout.html', context)
        
    except Cart.DoesNotExist:
        messages.error(request, 'No tienes un carrito activo.')
        return redirect('main:products')


@login_required
def invoice_detail_view(request, invoice_id):
    """Vista para mostrar detalles de la factura"""
    invoice = get_object_or_404(Invoice, pk=invoice_id, order__user=request.user)
    
    context = {
        'title': f'Factura {invoice.invoice_number} - Digit Soft',
        'invoice': invoice,
    }
    return render(request, 'main/invoices/detail.html', context)


@login_required
def invoice_pdf_view(request, invoice_id):
    """Vista para descargar factura como PDF (simplificada)"""
    from django.http import HttpResponse
    
    invoice = get_object_or_404(Invoice, pk=invoice_id, order__user=request.user)
    
    # Por ahora devolvemos un mensaje simple
    # TODO: Implementar generación de PDF con reportlab
    content = f"""
    DIGIT SOFT - Soluciones Tecnológicas
    
    FACTURA: {invoice.invoice_number}
    Fecha: {invoice.invoice_date.strftime('%d/%m/%Y')}
    Cliente: {invoice.order.user.get_full_name()}
    
    Productos:
    """
    
    for item in invoice.order.orderitem_set.all():
        content += f"\n- {item.quantity} x {item.product.name} - ${item.price:,.2f}"
    
    content += f"\n\nTOTAL: ${invoice.order.total_amount:,.2f}"
    
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="factura_{invoice.invoice_number}.txt"'
    
    return response
