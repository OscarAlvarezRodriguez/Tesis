# Gestor de Tareas - Proyecto experimental

Este repositorio contiene el proyecto base para el experimento académico de la tesis:
**"Impacto de la inteligencia artificial generativa en la implementación de Test Driven Development"**

El README y el demo solo muestran el funcionamiento básico actual.
Las funcionalidades nuevas y sus pruebas deben ser implementadas por el estudiante como parte del reto.

---

## Requisitos
- Python 3.x instalado (recomendado 3.8+)
- Acceso a terminal o consola (cmd / PowerShell / bash)

---

## Estructura inicial
- `gestor_tareas/tarea.py`: Clase Tarea con atributos básicos y método para marcar como completada.
- `gestor_tareas/gestor_tareas.py`: Clase GestorTareas con métodos para agregar, listar y completar tareas.
- `tests/test_gestor_tareas.py`: Pruebas unitarias básicas.
- `main.py`: Demo opcional del funcionamiento actual.
- `requirements-dev.txt`: Lista de herramientas para análisis de calidad de código.
- `setup_env.bat` / `setup_env.sh`: Scripts para configurar el entorno y ejecutar pruebas.
- `run_analysis.sh`: Script para ejecutar los análisis de calidad de código.

---

## Tu reto
Extiende este proyecto cumpliendo los requisitos indicados en el enunciado del experimento.
Recuerda que el demo y el README no contienen pistas sobre la solución; debes diseñarla y desarrollarla.

---

## Cómo instalar el proyecto y preparar el entorno

### Opción 1: Usando los scripts automáticos (recomendado)
#### En Windows:
```bash
setup_env.bat
```

#### En Linux/Mac:
```bash
bash setup_env.sh
```

### Opcion manual
```bash
python -m venv venv
source venv/bin/activate        # En Linux/Mac

# o

venv\Scripts\activate           # En Windows
```

Luego

```bash
pip install -r requirements-dev.txt
```

## Cómo ejecutar las pruebas
```bash
python -m unittest discover -s tests
```
o bien puedes ejecutar el script setup_env

## Para evaluar la calidad del código puedes ejecutar:
```bash
bash run_analysis.sh
```


## Cómo ejecutar el demo opcional (no necesario para el experimento)
```bash
python main.py
```

## Comentarios finales:
