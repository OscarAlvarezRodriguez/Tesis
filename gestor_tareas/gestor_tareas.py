from .tarea import Tarea


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea: Tarea):
        if any(t.tarea_id == tarea.tarea_id for t in self.tareas):
            raise ValueError(f"Ya existe una tarea con id={tarea.tarea_id}")
        self.tareas.append(tarea)

    def marcar_tarea_completada(self, tarea_id: int):
        for tarea in self.tareas:
            if tarea.tarea_id == tarea_id:
                tarea.marcar_completada()
                return True
        return False

    def listar_tareas(self):
        return self.tareas
