# Este demo main.py fue generado con ayuda de ChatGPT,
# en base a las clases Tarea y GestorTareas del proyecto.
# Su propósito es demostrar el uso de las funcionalidades implementadas,
# sin necesidad de modificaciones por parte del estudiante.
# El fin de este archivo es realmente dar una idea
# para que hagan pruebas manuales, sin embargo no es necesario modificarlo.


from gestor_tareas.gestor_tareas import GestorTareas
from gestor_tareas.tarea import Tarea


def demo():
    print("🌟 DEMO DEL GESTOR DE TAREAS 🌟\n")

    gestor = GestorTareas()

    # Crear tareas con auto-ID
    t1 = Tarea("Estudiar para examen")
    t2 = Tarea("Hacer ejercicio")
    t3 = Tarea("Leer un libro")

    # Agregar tareas al gestor
    gestor.agregar_tarea(t1)
    gestor.agregar_tarea(t2)
    gestor.agregar_tarea(t3)

    print("✅ Tareas actuales:")
    for t in gestor.listar_tareas():
        print(t)

    # Marcar una tarea como completada
    gestor.marcar_tarea_completada(t1.tarea_id)

    print("\n✅ Después de marcar como completada la tarea 1:")
    for t in gestor.listar_tareas():
        print(t)

    # Intentar agregar tarea con ID duplicado
    print("\n⚠ Intentando agregar tarea con ID duplicado:")
    try:
        t_dup = Tarea("Duplicada", tarea_id=t1.tarea_id)
        gestor.agregar_tarea(t_dup)
    except ValueError as ve:
        print(f"Error: {ve}")

    # Intentar crear tarea con nombre no string
    print("\n⚠ Intentando crear tarea con nombre inválido:")
    try:
        Tarea(1234)
    except TypeError as te:
        print(f"Error: {te}")

    # Listar tareas finales
    print("\n✅ Tareas finales en el gestor:")
    for t in gestor.listar_tareas():
        print(t)


if __name__ == "__main__":
    demo()
