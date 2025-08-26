from django import forms
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, DateInput, NumberInput
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import (
    Cliente, Marca, Proveedor, Administrador, Producto, Equipo, Tecnico,
    OrdenServicio, ServicioTecnico, Venta, ComprasMercancia, Facturacion, Garantias
)

def validate_description(description):
    """
    Valida que una descripción no esté vacía, no contenga solo números
    y tenga una longitud mínima de 10 caracteres.
    """
    if not description:
        raise ValidationError("La descripción no puede estar vacía.")
    if description.isdigit():
        raise ValidationError("La descripción no puede contener solo números.")
    if len(description) < 10:
        raise ValidationError("La descripción debe tener al menos 10 caracteres.")
    return description

class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'numero_documento': TextInput(attrs={'placeholder': 'Ingrese el número de documento'}),
            'numero_telefonico': TextInput(attrs={'placeholder': 'Ingrese el número telefónico'}),
            'correo_electronico': TextInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
        }

    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')
        if numero_documento and numero_documento == '0':
            raise ValidationError("El número de documento no puede ser '0'.")
        if numero_documento and Cliente.objects.filter(numero_documento=numero_documento).exists():
            raise ValidationError("Este número de documento ya está registrado.")
        return numero_documento

    def clean_numero_telefonico(self):
        numero_telefonico = self.cleaned_data.get('numero_telefonico')
        if numero_telefonico:
            if not numero_telefonico.isdigit():
                raise ValidationError("El número de teléfono debe contener solo dígitos.")
            if len(numero_telefonico) < 7:
                raise ValidationError("El número de teléfono debe tener al menos 7 dígitos.")
            if numero_telefonico == '0' or all(c == '0' for c in numero_telefonico):
                raise ValidationError("El número de teléfono no puede ser solo ceros.")
            if Cliente.objects.filter(numero_telefonico=numero_telefonico).exists():
                raise ValidationError("Este número de teléfono ya está registrado.")
        return numero_telefonico

    def clean_correo_electronico(self):
        correo = self.cleaned_data.get('correo_electronico')
        if correo:
            if Cliente.objects.filter(correo_electronico=correo).exists():
                raise ValidationError("Este correo electrónico ya está registrado.")
            try:
                validate_email(correo)
            except ValidationError:
                raise ValidationError("Ingrese un correo electrónico válido.")
        return correo

class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['marca'].widget.attrs['autofocus'] = True

    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'placeholder': 'Ingrese el color'}),
            'marca': TextInput(attrs={'placeholder': 'Ingrese la marca'}),
            'descripcion': Textarea(attrs={'placeholder': 'Ingrese una descripción', 'rows': 3, 'cols': 40}),
        }

    def clean_marca(self):
        marca = self.cleaned_data.get('marca')
        if marca and Marca.objects.filter(marca=marca).exists():
            raise ValidationError("Esta marca ya existe.")
        return marca

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion:
            return validate_description(descripcion)
        return descripcion

class ProveedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nit_proveedor': TextInput(attrs={'placeholder': 'Ingrese el NIT del proveedor'}),
            'nombre': TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'cedula': TextInput(attrs={'placeholder': 'Ingrese la cédula'}),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
            'telefono': TextInput(attrs={'placeholder': 'Ingrese el teléfono'}),
        }

    def clean_nit_proveedor(self):
        nit = self.cleaned_data.get('nit_proveedor')
        if nit and Proveedor.objects.filter(nit_proveedor=nit).exists():
            raise ValidationError("Este NIT ya está registrado.")
        return nit

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if cedula and cedula == '0':
            raise ValidationError("La cédula no puede ser '0'.")
        if cedula and Proveedor.objects.filter(cedula=cedula).exists():
            raise ValidationError("Esta cédula ya está registrada.")
        return cedula

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono:
            if not telefono.isdigit():
                raise ValidationError("El número de teléfono debe contener solo dígitos.")
            if len(telefono) < 7:
                raise ValidationError("El número de teléfono debe tener al menos 7 dígitos.")
            if telefono == '0' or all(c == '0' for c in telefono):
                raise ValidationError("El número de teléfono no puede ser solo ceros.")
            if Proveedor.objects.filter(telefono=telefono).exists():
                raise ValidationError("Este número de teléfono ya está registrado.")
        return telefono

class AdministradorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Administrador
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'contrasena': PasswordInput(attrs={'placeholder': 'Ingrese la contraseña'}),
            'correo_electronico': TextInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
        }

    def clean_correo_electronico(self):
        correo = self.cleaned_data.get('correo_electronico')
        if correo:
            if Administrador.objects.filter(correo_electronico=correo).exists():
                raise ValidationError("Este correo electrónico ya está registrado.")
            try:
                validate_email(correo)
            except ValidationError:
                raise ValidationError("Ingrese un correo electrónico válido.")
        return correo

    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')
        if contrasena and len(contrasena) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return contrasena

class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_producto'].widget.attrs['autofocus'] = True

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre_producto': TextInput(attrs={'placeholder': 'Ingrese el nombre del producto'}),
            'modelo_producto': TextInput(attrs={'placeholder': 'Ingrese el modelo'}),
            'cantidad': NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'valor_producto': TextInput(attrs={'placeholder': 'Ingrese el valor'}),
            'diseno': TextInput(attrs={'placeholder': 'Ingrese el diseño'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre_producto')
        modelo = cleaned_data.get('modelo_producto')
        if nombre and modelo and Producto.objects.filter(nombre_producto=nombre, modelo_producto=modelo).exists():
            raise ValidationError("Ya existe un producto con este nombre y modelo.")
        return cleaned_data

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad and cantidad < 0:
            raise ValidationError("La cantidad no puede ser un número negativo.")
        return cantidad

class EquipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'modelo': TextInput(attrs={'placeholder': 'Ingrese el modelo'}),
            'clave': TextInput(attrs={'placeholder': 'Ingrese la clave'}),
        }

    def clean_modelo(self):
        modelo = self.cleaned_data.get('modelo')
        if modelo and Equipo.objects.filter(modelo=modelo).exists():
            raise ValidationError("Ya existe un equipo con este modelo.")
        return modelo

class TecnicoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_completo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Tecnico
        fields = '__all__'
        widgets = {
            'nombre_completo': TextInput(attrs={'placeholder': 'Ingrese el nombre completo'}),
            'n_documento': NumberInput(attrs={'placeholder': 'Ingrese el número de documento'}),
            'n_tel': NumberInput(attrs={'placeholder': 'Ingrese el teléfono'}),
            'correo': TextInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
            'especialidad': TextInput(attrs={'placeholder': 'Ingrese la especialidad'}),
            'tipo_tecnico': TextInput(attrs={'placeholder': 'Ingrese el tipo de técnico'}),
        }

    def clean_n_documento(self):
        n_documento = self.cleaned_data.get('n_documento')
        if n_documento == 0:
            raise ValidationError("El número de documento no puede ser '0'.")
        if n_documento and Tecnico.objects.filter(n_documento=n_documento).exists():
            raise ValidationError("Este número de documento ya está registrado.")
        return n_documento

    def clean_n_tel(self):
        n_tel = self.cleaned_data.get('n_tel')
        if n_tel:
            if not str(n_tel).isdigit():
                raise ValidationError("El número de teléfono debe contener solo dígitos.")
            if len(str(n_tel)) < 7:
                raise ValidationError("El número de teléfono debe tener al menos 7 dígitos.")
            if n_tel == 0 or all(c == '0' for c in str(n_tel)):
                raise ValidationError("El número de teléfono no puede ser solo ceros.")
            if Tecnico.objects.filter(n_tel=n_tel).exists():
                raise ValidationError("Este número de teléfono ya está registrado.")
        return n_tel

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if correo:
            if Tecnico.objects.filter(correo=correo).exists():
                raise ValidationError("Este correo electrónico ya está registrado.")
            try:
                validate_email(correo)
            except ValidationError:
                raise ValidationError("Ingrese un correo electrónico válido.")
        return correo

class OrdenServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion_orden'].widget.attrs['autofocus'] = True

    class Meta:
        model = OrdenServicio
        fields = '__all__'
        widgets = {
            'descripcion_orden': Textarea(attrs={'placeholder': 'Ingrese la descripción', 'rows': 3, 'cols': 40}),
        }
    
    def clean_descripcion_orden(self):
        descripcion_orden = self.cleaned_data.get('descripcion_orden')
        if descripcion_orden:
            return validate_description(descripcion_orden)
        return descripcion_orden

class ServicioTecnicoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion_falla'].widget.attrs['autofocus'] = True

    class Meta:
        model = ServicioTecnico
        fields = '__all__'
        widgets = {
            'equipo': TextInput(attrs={'placeholder': 'Ingrese el equipo'}),
            'descripcion_falla': Textarea(attrs={'placeholder': 'Describa la falla', 'rows': 3, 'cols': 40}),
            'fecha_ingreso': DateInput(attrs={'type': 'date'}),
            'fecha_entrega': DateInput(attrs={'type': 'date'}),
            'estado': TextInput(attrs={'placeholder': 'Ingrese el estado'}),
        }
    
    def clean_descripcion_falla(self):
        descripcion_falla = self.cleaned_data.get('descripcion_falla')
        if descripcion_falla:
            return validate_description(descripcion_falla)
        return descripcion_falla

class VentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_venta'].widget.attrs['autofocus'] = True

    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'fecha_venta': DateInput(attrs={'type': 'date'}),
            'cantidad': NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'total': NumberInput(attrs={'placeholder': 'Ingrese el total'}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad and cantidad <= 0:
            raise ValidationError("La cantidad debe ser mayor que cero.")
        return cantidad

    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total and total <= 0:
            raise ValidationError("El total debe ser mayor que cero.")
        return total

class ComprasMercanciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cantidad_compras'].widget.attrs['autofocus'] = True

    class Meta:
        model = ComprasMercancia
        fields = '__all__'
        widgets = {
            'cantidad_compras': NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'fecha_compra': DateInput(attrs={'type': 'date'}),
            'precio_compra': TextInput(attrs={'placeholder': 'Ingrese el precio de compra'}),
        }

    def clean_cantidad_compras(self):
        cantidad = self.cleaned_data.get('cantidad_compras')
        if cantidad and cantidad <= 0:
            raise ValidationError("La cantidad de compras debe ser mayor que cero.")
        return cantidad

    def clean_precio_compra(self):
        precio = self.cleaned_data.get('precio_compra')
        if precio:
            try:
                precio_float = float(precio)
                if precio_float < 0:
                    raise ValidationError("El precio de compra no puede ser negativo.")
            except (ValueError, TypeError):
                raise ValidationError("Ingrese un valor numérico para el precio.")
        return precio

class FacturacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs['autofocus'] = True

    class Meta:
        model = Facturacion
        fields = '__all__'
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
            'descripcion_venta': Textarea(attrs={'placeholder': 'Ingrese una descripción', 'rows': 3, 'cols': 40}),
            'terminos_y_condiciones': Textarea(attrs={'placeholder': 'Ingrese los términos y condiciones', 'rows': 3, 'cols': 40}),
            'nit_digisoft': TextInput(attrs={'placeholder': 'Ingrese el NIT'}),
        }
    
    def clean_descripcion_venta(self):
        descripcion_venta = self.cleaned_data.get('descripcion_venta')
        if descripcion_venta:
            return validate_description(descripcion_venta)
        return descripcion_venta

    def clean_nit_digisoft(self):
        nit = self.cleaned_data.get('nit_digisoft')
        if nit:
            if nit == '0' or all(c == '0' for c in nit):
                raise ValidationError("El NIT no puede ser solo ceros.")
            if not nit.isdigit():
                raise ValidationError("El NIT debe contener solo dígitos.")
        return nit

class GarantiasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['facturacion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Garantias
        fields = '__all__'
        widgets = {
            'facturacion': TextInput(attrs={'placeholder': 'Ingrese la facturación'}),
            'fecha_fin': DateInput(attrs={'type': 'date'}),
            'terminos': Textarea(attrs={'placeholder': 'Términos de la garantía', 'rows': 3, 'cols': 40}),
        }

    def clean_terminos(self):
        terminos = self.cleaned_data.get('terminos')
        if terminos:
            return validate_description(terminos)
        return terminos