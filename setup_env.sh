#!/bin/bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

echo "Entorno virtual activado."

# Instalar dependencias desde requirements-dev.txt
echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Instalación completa. El entorno está listo."

# Ejecutar pruebas automáticamente
echo "Ejecutando pruebas..."
python -m unittest discover -s tests

echo "Setup finalizado."
