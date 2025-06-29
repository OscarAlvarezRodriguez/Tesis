@echo off
REM Crear entorno virtual
python -m venv venv
call venv\Scripts\activate

echo Entorno virtual activado.

REM Instalar dependencias desde requirements-dev.txt
echo Instalando dependencias...
pip install -r requirements-dev.txt

echo Instalación completa. El entorno está listo.

REM Ejecutar pruebas automáticamente
echo Ejecutando pruebas...
python -m unittest discover -s tests

echo Setup finalizado.
