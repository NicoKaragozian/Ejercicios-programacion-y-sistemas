#%%
# Importamos las funciones desde el script principal
from semana_02 import (
    invertir_lista,
    collatz,
    contar_definiciones,
    cantidad_de_claves_letra,
    propagar
)

import unittest

# ---------- TEST PARA INVERTIR LISTA ----------
class TestInvertirLista(unittest.TestCase):

    def test_lista_numerica(self):
        self.assertEqual(invertir_lista([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_lista_strings(self):
        self.assertEqual(invertir_lista(['a', 'b', 'c']), ['c', 'b', 'a'])

    def test_lista_vacia(self):
        self.assertEqual(invertir_lista([]), [])

# ---------- TEST PARA COLLATZ ----------
class TestCollatz(unittest.TestCase):

    def test_numero_positivo(self):
        self.assertEqual(collatz(6), 8)

    def test_numero_uno(self):
        self.assertEqual(collatz(1), 0)

    def test_error_numero_negativo(self):
        with self.assertRaises(ValueError):
            collatz(-5)

# ---------- TEST PARA CONTAR DEFINICIONES ----------
class TestContarDefiniciones(unittest.TestCase):

    def test_diccionario_con_definiciones(self):
        d = {
            "River": ["Gallardo", "Libertadores"],
            "Boca": ["Gago", "Nada", "Tristeza"],
        }
        self.assertEqual(contar_definiciones(d), {"River": 2, "Boca": 3})

    def test_diccionario_con_definiciones2(self):
        d = {
            "Lobo": ["Caza", "Montaña"],
            "Leon": ["Selva", "Rey"],
            "Tigre": ["Selva"]
        }
        self.assertEqual(contar_definiciones(d), {"Lobo": 2, "Leon": 2, "Tigre": 1})

    def test_diccionario_vacio(self):
        d = {}
        self.assertEqual(contar_definiciones(d), {})

# ---------- TEST PARA CANTIDAD DE CLAVES POR LETRA ----------
class TestCantidadClavesLetra(unittest.TestCase):

    def test_claves_con_letra(self):
        d = {
            "Lobo": ["Caza", "Montaña"],
            "Leon": ["Selva", "Rey"],
            "Tigre": ["Selva"]
        }
        self.assertEqual(cantidad_de_claves_letra(d, "L"), 2)

    def test_claves_con_letra2(self):
        d = {
            "River": ["Gallardo", "Libertadores"],
            "Boca": ["Gago", "Nada", "Tristeza"],
        }
        self.assertEqual(cantidad_de_claves_letra(d, "R"), 1)

    def test_claves_sin_coincidencia(self):
        d = {"Perro": ["Casa"]}
        self.assertEqual(cantidad_de_claves_letra(d, "Z"), 0)

# ---------- TEST PARA PROPAGAR ----------
class TestPropagar(unittest.TestCase):

    def test_propagacion_completa(self):
        fosforos = [0, 0, 1, 0, 0]
        self.assertEqual(propagar(fosforos), [1, 1, 1, 1, 1])

    def test_propagacion_interrumpida(self):
        fosforos = [0, 0, -1, 1, 0, 0]
        self.assertEqual(propagar(fosforos), [0, 0, -1, 1, 1, 1])

    def test_sin_propagacion(self):
        fosforos = [-1, 0, 0, -1]
        self.assertEqual(propagar(fosforos), [-1, 0, 0, -1])

# ---------- CORRER LOS TESTS ----------
if __name__ == '__main__':
    unittest.main()

# %%
