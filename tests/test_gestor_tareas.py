import unittest
from gestor_tareas.gestor_tareas import GestorTareas
from gestor_tareas.tarea import Tarea, ESTADO_PENDIENTE, ESTADO_COMPLETADA


class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTareas()

    def test_agregar_tarea_correctamente(self):
        tarea = Tarea("Estudiar para examen", tarea_id=1)
        self.gestor.agregar_tarea(tarea)
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0].estado, ESTADO_PENDIENTE)

    def test_agregar_tarea_id_duplicado(self):
        tarea1 = Tarea("Tarea 1", tarea_id=1)
        tarea2 = Tarea("Tarea 2", tarea_id=1)
        self.gestor.agregar_tarea(tarea1)
        with self.assertRaises(ValueError):
            self.gestor.agregar_tarea(tarea2)

    def test_auto_id_incremental(self):
        tarea1 = Tarea("Tarea auto 1")
        tarea2 = Tarea("Tarea auto 2")
        self.gestor.agregar_tarea(tarea1)
        self.gestor.agregar_tarea(tarea2)
        self.assertNotEqual(tarea1.tarea_id, tarea2.tarea_id)

    def test_nombre_no_es_string(self):
        with self.assertRaises(TypeError):
            Tarea(1234)

    def test_marcar_tarea_completada_existente(self):
        tarea = Tarea("Completar tarea", tarea_id=10)
        self.gestor.agregar_tarea(tarea)
        result = self.gestor.marcar_tarea_completada(10)
        self.assertTrue(result)
        self.assertEqual(self.gestor.tareas[0].estado, ESTADO_COMPLETADA)

    def test_marcar_tarea_completada_inexistente(self):
        result = self.gestor.marcar_tarea_completada(999)
        self.assertFalse(result)

    def test_listar_tareas_devuelve_correcto(self):
        tarea1 = Tarea("Tarea A")
        tarea2 = Tarea("Tarea B")
        self.gestor.agregar_tarea(tarea1)
        self.gestor.agregar_tarea(tarea2)
        lista = self.gestor.listar_tareas()
        self.assertEqual(len(lista), 2)
        self.assertIn(tarea1, lista)
        self.assertIn(tarea2, lista)


if __name__ == '__main__':
    unittest.main()
