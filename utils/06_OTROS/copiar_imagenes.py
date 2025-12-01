import shutil
from pathlib import Path

origen = Path('C:/Users/jorge/OneDrive/Escritorio/DigitSoftAdelanto/Digit_Sof_Nuevo/static/imagenes')
destino = Path('C:/Users/jorge/OneDrive/Escritorio/DigitSoftAdelanto/Digit_Sof_Nuevo/static/images')

# Crear carpeta destino
destino.mkdir(exist_ok=True)

# Copiar todas las imágenes
contador = 0
for archivo in origen.glob('*'):
    if archivo.is_file():
        shutil.copy2(str(archivo), str(destino / archivo.name))
        print(f"✅ Copiado: {archivo.name}")
        contador += 1

print(f"\n✅ Total: {contador} imágenes copiadas a static/images/")

