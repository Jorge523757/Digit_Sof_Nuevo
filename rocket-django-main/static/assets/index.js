import './style.css';
import 'flowbite/dist/flowbite.js';
import './sidebar';
import './charts';
import './dark-mode';

// --- Array de productos compartido ---
window.productos = [
    {
        id: 1,
        nombre: 'Laptop HP Pavilion Gaming',
        categoria: 'laptop',
        precio: 2500000,
        marca: 'HP',
        descripcion: 'Laptop gaming de alto rendimiento...',
        imagen: '/static/dashboard/img/laptop_hp_pavilion.jpg',
        especificaciones: ['Intel Core i5-10300H', '16GB RAM DDR4', 'SSD 512GB NVMe', 'NVIDIA GTX 1650Ti 4GB', 'Pantalla 15.6" Full HD IPS']
    },
    // ...agrega aquí más productos...
];

// --- Renderizar tabla de productos ---
window.onload = function() {
    const tbody = document.getElementById('tablaProductosBody');
    if (tbody && window.productos) {
        window.productos.forEach(producto => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${producto.nombre}</td>
                <td>${producto.marca}</td>
                <td>${producto.precio.toLocaleString('es-CO')}</td>
                <td><img src="${producto.imagen}" alt="${producto.nombre}" width="80"></td>
                <td>
                    <button onclick="agregarProductoVenta(${producto.id})" class="btn btn-success btn-sm">Agregar a venta</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    }
};

// --- Lógica de venta ---
window.productosVenta = [];

window.agregarProductoVenta = function(productId) {
    const producto = window.productos.find(p => p.id === productId);
    if (!producto) return;
    const existente = window.productosVenta.find(p => p.id === productId);
    if (existente) {
        existente.cantidad++;
    } else {
        window.productosVenta.push({ ...producto, cantidad: 1 });
    }
    actualizarTablaVenta();
};

window.actualizarTablaVenta = function() {
    const tbody = document.getElementById('tablaVentaBody');
    if (!tbody) return;
    tbody.innerHTML = window.productosVenta.map(p => `
        <tr>
            <td>${p.nombre}</td>
            <td>${p.marca}</td>
            <td>${p.precio.toLocaleString('es-CO')}</td>
            <td>${p.cantidad}</td>
            <td>${(p.precio * p.cantidad).toLocaleString('es-CO')}</td>
            <td>
                <button onclick="eliminarProductoVenta(${p.id})" class="btn btn-danger btn-sm">Eliminar</button>
            </td>
        </tr>
    `).join('');
};

window.eliminarProductoVenta = function(productId) {
    window.productosVenta = window.productosVenta.filter(p => p.id !== productId);
    actualizarTablaVenta();
};

// --- Guardar venta y generar factura PDF ---
window.guardarVenta = function() {
    if (window.productosVenta.length === 0) {
        alert('No hay productos en la venta');
        return;
    }
    const venta = {
        id_venta: Date.now(),
        productos: window.productosVenta,
        total: window.productosVenta.reduce((sum, p) => sum + p.precio * p.cantidad, 0),
        fecha: new Date().toLocaleDateString()
    };
    generarFacturaPDF(venta);
    window.productosVenta = [];
    actualizarTablaVenta();
    alert('Venta guardada y factura generada');
};

window.generarFacturaPDF = function(venta) {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    doc.setFontSize(22);
    doc.text('DigitSoft - Factura', 20, 20);
    doc.setFontSize(12);
    doc.text(`ID Venta: ${venta.id_venta}`, 20, 30);
    doc.text(`Fecha: ${venta.fecha}`, 20, 36);

    // Tabla de productos
    doc.text('Productos:', 20, 46);
    let y = 52;
    doc.text('Cant.', 20, y);
    doc.text('Nombre', 35, y);
    doc.text('Marca', 90, y);
    doc.text('Precio', 120, y);
    doc.text('Subtotal', 150, y);
    y += 6;
    venta.productos.forEach(p => {
        doc.text(`${p.cantidad}`, 20, y);
        doc.text(`${p.nombre}`, 35, y);
        doc.text(`${p.marca}`, 90, y);
        doc.text(`$${p.precio.toLocaleString('es-CO')}`, 120, y);
        doc.text(`$${(p.precio * p.cantidad).toLocaleString('es-CO')}`, 150, y);
        y += 6;
    });

    doc.setFontSize(14);
    doc.text(`TOTAL: $${venta.total.toLocaleString('es-CO')}`, 120, y + 10);

    doc.save(`DigitSoft_Factura_${venta.id_venta}.pdf`);
};
