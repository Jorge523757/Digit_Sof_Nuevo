@echo off
echo ============================================
echo  PRUEBA: PRECIOS EN PESOS COLOMBIANOS
echo ============================================
echo.
echo Este script te ayudara a verificar los cambios
echo.
echo PASOS A SEGUIR:
echo.
echo 1. Asegurate de que el servidor este corriendo
echo 2. Ve a: http://localhost:8000/ordenes/crear/
echo 3. Prueba escribir en "Costo de Diagnostico": 50000
echo 4. Deberas ver automaticamente: 50.000
echo 5. Prueba escribir en "Costo de Mano de Obra": 100000
echo 6. Deberas ver automaticamente: 100.000
echo.
echo ============================================
echo  INICIANDO SERVIDOR...
echo ============================================
echo.

python manage.py runserver

pause

