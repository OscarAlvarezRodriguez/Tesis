@echo off
:: Crear un entorno virtual
python -m venv venv
call venv\Scripts\activate.bat
echo Entorno virtual activado.

:: Análisis de estilo con flake8
echo ▶ Análisis de estilo con flake8:
flake8 gestor_tareas tests main.py

echo.
echo ▶ Análisis de estilo y convenciones con pylint:
pylint gestor_tareas tests main.py

echo.
echo ▶ Análisis de complejidad ciclomática con radon:
radon cc gestor_tareas tests main.py -a

echo.
echo ▶ Análisis de mantenibilidad con radon:
radon mi gestor_tareas tests main.py

echo.
echo ▶ Análisis de seguridad con bandit:
bandit -r gestor_tareas

echo.
echo ✅ Análisis completo.
echo Setup finalizado.
