#!/bin/bash

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

clear

echo ""
echo "══════════════════════════════════════════════════════════════"
echo "          INSTALACIÓN COMPLETA - DIGIT SOFT"
echo "══════════════════════════════════════════════════════════════"
echo ""

# Verificar Python
echo -e "${BLUE}[1/6] Verificando Python...${NC}"
if command -v python3 &> /dev/null; then
    python3 --version
    echo -e "${GREEN}✅ Python encontrado${NC}"
else
    echo -e "${RED}❌ Python no está instalado${NC}"
    exit 1
fi
echo ""

# Crear entorno virtual
echo -e "${BLUE}[2/6] Creando entorno virtual...${NC}"
if [ -d "venv" ]; then
    echo -e "${YELLOW}⚠️  Entorno virtual ya existe, omitiendo...${NC}"
else
    python3 -m venv venv
    echo -e "${GREEN}✅ Entorno virtual creado${NC}"
fi
echo ""

# Activar entorno virtual
echo -e "${BLUE}[3/6] Activando entorno virtual...${NC}"
source venv/bin/activate
echo -e "${GREEN}✅ Entorno activado${NC}"
echo ""

# Instalar dependencias
echo -e "${BLUE}[4/6] Instalando dependencias...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}✅ Dependencias instaladas${NC}"
echo ""

# Aplicar migraciones
echo -e "${BLUE}[5/6] Aplicando migraciones...${NC}"
python manage.py migrate
echo -e "${GREEN}✅ Base de datos configurada${NC}"
echo ""

# Crear superusuario
echo -e "${BLUE}[6/6] Creando superusuario...${NC}"
python crear_superusuario.py
echo ""

echo "══════════════════════════════════════════════════════════════"
echo -e "${GREEN}          ✅ INSTALACIÓN COMPLETADA${NC}"
echo "══════════════════════════════════════════════════════════════"
echo ""
echo "Para iniciar el servidor:"
echo "   source venv/bin/activate"
echo "   python manage.py runserver"
echo ""
echo "Luego accede a: http://127.0.0.1:8000"
echo ""
echo "Usuario: admin"
echo "Contraseña: admin123"
echo ""
echo "══════════════════════════════════════════════════════════════"
echo ""

