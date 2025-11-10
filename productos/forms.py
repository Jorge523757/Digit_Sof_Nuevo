"""
DIGT SOFT - Formularios del Módulo de Productos
"""

from django import forms
from .models import Producto, CategoriaProducto, MovimientoInventario


class ProductoForm(forms.ModelForm):
    """Formulario para crear y editar productos"""

    class Meta:
        model = Producto
        fields = [
            'nombre_producto', 'codigo_sku', 'categoria',
            'modelo_equipo', 'marca', 'procesador', 'memoria_ram', 'memoria_rom',
            'descripcion', 'especificaciones',
            'precio_compra', 'precio_venta', 'precio_mayorista',
            'stock_actual', 'stock_minimo', 'stock_maximo',
            'imagen', 'disponible_web', 'destacado',
            'tiene_garantia', 'meses_garantia', 'activo'
        ]
        widgets = {
            'nombre_producto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Laptop Dell Inspiron 15',
                'required': True
            }),
            'codigo_sku': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: PROD-001',
                'required': True
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'modelo_equipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Inspiron 15 3000'
            }),
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Dell'
            }),
            'procesador': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Intel Core i5 11va Gen'
            }),
            'memoria_ram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 8GB DDR4'
            }),
            'memoria_rom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 256GB SSD'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción detallada del producto...',
                'required': True
            }),
            'especificaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Especificaciones técnicas adicionales...'
            }),
            'precio_compra': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01',
                'required': True
            }),
            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01',
                'required': True
            }),
            'precio_mayorista': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01'
            }),
            'stock_actual': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0',
                'required': True
            }),
            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '5',
                'min': '0',
                'required': True
            }),
            'stock_maximo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '100',
                'min': '0',
                'required': True
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'disponible_web': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'destacado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'tiene_garantia': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'meses_garantia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '12',
                'min': '0'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def clean_codigo_sku(self):
        """Valida que el código SKU sea único"""
        codigo = self.cleaned_data.get('codigo_sku')
        if codigo:
            codigo = codigo.upper().strip()
            # Si es edición, excluir el producto actual
            if self.instance and self.instance.pk:
                if Producto.objects.filter(codigo_sku=codigo).exclude(pk=self.instance.pk).exists():
                    raise forms.ValidationError('Ya existe un producto con este código SKU.')
            else:
                if Producto.objects.filter(codigo_sku=codigo).exists():
                    raise forms.ValidationError('Ya existe un producto con este código SKU.')
        return codigo

    def clean(self):
        """Validaciones adicionales"""
        cleaned_data = super().clean()
        precio_compra = cleaned_data.get('precio_compra')
        precio_venta = cleaned_data.get('precio_venta')
        precio_mayorista = cleaned_data.get('precio_mayorista')
        stock_minimo = cleaned_data.get('stock_minimo')
        stock_maximo = cleaned_data.get('stock_maximo')

        # Validar que el precio de venta sea mayor al de compra
        if precio_compra and precio_venta:
            if precio_venta <= precio_compra:
                raise forms.ValidationError('El precio de venta debe ser mayor al precio de compra.')

        # Validar precio mayorista
        if precio_mayorista and precio_compra:
            if precio_mayorista < precio_compra:
                raise forms.ValidationError('El precio mayorista no puede ser menor al precio de compra.')

        # Validar stock
        if stock_minimo and stock_maximo:
            if stock_minimo > stock_maximo:
                raise forms.ValidationError('El stock mínimo no puede ser mayor al stock máximo.')

        return cleaned_data


class CategoriaProductoForm(forms.ModelForm):
    """Formulario para categorías de productos"""

    class Meta:
        model = CategoriaProducto
        fields = ['nombre', 'descripcion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la categoría',
                'required': True
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción de la categoría...'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }


class MovimientoInventarioForm(forms.ModelForm):
    """Formulario para registrar movimientos de inventario"""

    class Meta:
        model = MovimientoInventario
        fields = ['producto', 'tipo_movimiento', 'cantidad', 'motivo', 'observaciones']
        widgets = {
            'producto': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'tipo_movimiento': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1',
                'min': '1',
                'required': True
            }),
            'motivo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Compra a proveedor, Venta a cliente...',
                'required': True
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales...'
            }),
        }


class BuscarProductoForm(forms.Form):
    """Formulario para búsqueda de productos"""

    busqueda = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '🔍 Buscar por nombre, código SKU, marca...',
            'id': 'busqueda-producto'
        })
    )
    categoria = forms.ModelChoiceField(
        queryset=CategoriaProducto.objects.filter(activo=True),
        required=False,
        empty_label="Todas las categorías",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    estado = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Todos'),
            ('activo', 'Activos'),
            ('inactivo', 'Inactivos'),
            ('bajo_stock', 'Bajo stock'),
            ('sin_stock', 'Sin stock'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

