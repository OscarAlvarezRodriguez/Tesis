import itertools

# Constantes globales para estados de Tarea
ESTADO_PENDIENTE = "pendiente"
ESTADO_COMPLETADA = "completada"

# Generador incremental de ID (en memoria, para el demo)
_id_generator = itertools.count(1)


class Tarea:
    def __init__(self, nombre: str, tarea_id: int = None):
        if not isinstance(nombre, str):
            raise TypeError("El nombre de la tarea debe ser un string.")
        self.tarea_id = (
            tarea_id if tarea_id is not None else next(_id_generator)
        )
        self.nombre = nombre
        self.estado = ESTADO_PENDIENTE

    def marcar_completada(self):
        self.estado = ESTADO_COMPLETADA

    def __str__(self):
        return (
            f"Tarea(id={self.tarea_id}, \
            nombre='{self.nombre}', \
            estado='{self.estado}' \
            )"
        )
