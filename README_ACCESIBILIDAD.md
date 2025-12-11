# ♿ Sistema de Accesibilidad Web - DIGT SOFT

## 🎯 Implementación Completa y Funcional

Este documento contiene información rápida sobre el **Sistema de Accesibilidad** implementado en DIGT SOFT.

---

## 🚀 Inicio Rápido

### 1. Verificar Instalación
```bash
# Ejecutar el verificador
VERIFICAR_ACCESIBILIDAD.bat
```

### 2. Iniciar Servidor
```bash
# Opción 1: Usando el script
INICIAR_CON_ACCESIBILIDAD.bat

# Opción 2: Comando manual
python manage.py runserver
```

### 3. Probar el Sistema
1. Abrir navegador: `http://127.0.0.1:8000/`
2. Buscar botón flotante (♿) en esquina inferior derecha
3. Hacer clic y probar las opciones

---

## 📚 Documentación Disponible

### Archivos de Documentación:

1. **`README_ACCESIBILIDAD.md`** (Este archivo)
   - Inicio rápido y enlaces a documentación

2. **`GUIA_RAPIDA_ACCESIBILIDAD.md`**
   - Guía rápida de uso
   - Solución de problemas
   - Checklist de verificación

3. **`SISTEMA_ACCESIBILIDAD_COMPLETO.md`**
   - Documentación técnica completa
   - Todas las características detalladas
   - Referencias a estándares WCAG

4. **`RESUMEN_IMPLEMENTACION_ACCESIBILIDAD.md`**
   - Resumen ejecutivo
   - Lista de archivos modificados
   - Checklist de implementación

---

## ✨ Características Principales

### 🔤 Tamaño de Texto
- Aumentar: `Ctrl + Alt + +`
- Reducir: `Ctrl + Alt + -`
- Rango: 80% - 140%

### 🎨 Modos Visuales
- **Alto Contraste**: Mejora visibilidad
- **Modo Oscuro**: Reduce fatiga (`Ctrl + Alt + D`)
- **Escala de Grises**: Para daltonismo

### 🔗 Navegación
- **Resaltar Enlaces**: Fondo amarillo
- **Espaciado Aumentado**: Mejor legibilidad
- **Lector de Pantalla**: Compatible con NVDA, JAWS

### 🔄 Restablecer
- Volver a valores por defecto: `Ctrl + Alt + R`

---

## 📁 Estructura de Archivos

```
Digit_Sof_Nuevo/
├── templates/
│   ├── base.html                         ✅ Incluye accesibilidad
│   ├── base_dashboard.html               ✅ Incluye accesibilidad
│   └── includes/
│       └── accessibility_widget.html     ✅ Widget principal
│
├── static/
│   ├── css/
│   │   └── accessibility.css             ✅ Estilos completos
│   └── js/
│       └── accessibility.js              ✅ Funcionalidad completa
│
├── README_ACCESIBILIDAD.md               ✅ Este archivo
├── GUIA_RAPIDA_ACCESIBILIDAD.md          ✅ Guía rápida
├── SISTEMA_ACCESIBILIDAD_COMPLETO.md     ✅ Documentación técnica
├── RESUMEN_IMPLEMENTACION_ACCESIBILIDAD.md ✅ Resumen ejecutivo
├── INICIAR_CON_ACCESIBILIDAD.bat         ✅ Script de inicio
└── VERIFICAR_ACCESIBILIDAD.bat           ✅ Verificador
```

---

## ⌨️ Atajos de Teclado

| Atajo | Acción |
|-------|--------|
| `Ctrl + Alt + +` | Aumentar tamaño de texto |
| `Ctrl + Alt + -` | Reducir tamaño de texto |
| `Ctrl + Alt + D` | Toggle modo oscuro |
| `Ctrl + Alt + R` | Restablecer todo |
| `Tab` | Navegar entre elementos |
| `Esc` | Cerrar panel de accesibilidad |

---

## ✅ Estándares Cumplidos

- ✅ **WCAG 2.1 Nivel AA** (Completo)
- ✅ **WCAG 2.1 Nivel AAA** (Parcial)
- ✅ **Section 508** (EE.UU.)
- ✅ **EN 301 549** (Europa)

---

## 🔧 Archivos Principales

### HTML
- `templates/includes/accessibility_widget.html` - Widget reutilizable

### CSS
- `static/css/accessibility.css` - Todos los estilos

### JavaScript
- `static/js/accessibility.js` - Toda la funcionalidad

---

## 🧪 Probar el Sistema

### Checklist Rápido:
- [ ] Botón flotante visible en esquina inferior derecha
- [ ] Panel se abre al hacer clic
- [ ] Modo oscuro funciona (`Ctrl + Alt + D`)
- [ ] Tamaño de texto cambia con +/-
- [ ] Notificaciones aparecen al activar opciones
- [ ] Preferencias persisten al recargar página
- [ ] Todo es navegable con `Tab`

---

## 🐛 Solución de Problemas

### ❌ El widget no aparece
```bash
# 1. Verificar archivos
VERIFICAR_ACCESIBILIDAD.bat

# 2. Recolectar archivos estáticos
python manage.py collectstatic --noinput

# 3. Reiniciar servidor
python manage.py runserver
```

### ❌ Los estilos no se aplican
```bash
# Limpiar caché y recargar
Ctrl + F5 (en navegador)
```

### ❌ Errores de JavaScript
```bash
# Abrir consola del navegador
F12 > Console
# Verificar errores
```

---

## 📱 Compatibilidad

### Navegadores:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

### Dispositivos:
- ✅ Desktop
- ✅ Tablet
- ✅ Móvil

### Lectores de Pantalla:
- ✅ NVDA
- ✅ JAWS
- ✅ VoiceOver
- ✅ TalkBack

---

## 📞 Soporte

**Email:** accesibilidad@digitsoft.com.co  
**Teléfono:** (+57) 3215434380  
**Ubicación:** Calle 15 # 14-26, Duitama - Boyacá

---

## 🎓 Recursos de Aprendizaje

### Documentación Interna:
1. Lee `GUIA_RAPIDA_ACCESIBILIDAD.md` para empezar
2. Revisa `SISTEMA_ACCESIBILIDAD_COMPLETO.md` para detalles técnicos
3. Consulta `RESUMEN_IMPLEMENTACION_ACCESIBILIDAD.md` para overview

### Recursos Externos:
- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WebAIM](https://webaim.org/)

---

## 🎉 ¡Listo para Usar!

El sistema está **100% funcional** y listo para mejorar la experiencia de todos los usuarios.

### Comandos Útiles:
```bash
# Verificar instalación
VERIFICAR_ACCESIBILIDAD.bat

# Iniciar servidor
INICIAR_CON_ACCESIBILIDAD.bat
# o
python manage.py runserver

# Recolectar estáticos (producción)
python manage.py collectstatic --noinput
```

---

**Versión:** 1.0.0  
**Estado:** ✅ Producción  
**Última actualización:** 03 de Diciembre de 2025

---

> **"Accesibilidad es diseñar para todos, no solo para algunos."**

♿ Sistema de Accesibilidad - DIGT SOFT

