import unittest
from src.tablero import Tablero


class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
    
    def test_inicializacion(self):
        """Verifica que el tablero se inicializa vacío"""
        for fila in self.tablero.casillas:
            for casilla in fila:
                self.assertEqual(casilla, " ")
    
    def test_colocar_ficha_exitoso(self):
        """Verifica colocar ficha en casilla vacía"""
        resultado = self.tablero.colocar_ficha(1, 1, "X")
        self.assertTrue(resultado)
        self.assertEqual(self.tablero.casillas[1][1], "X")
    
    def test_colocar_ficha_casilla_ocupada(self):
        """Verifica que no se puede colocar ficha en casilla ocupada"""
        self.tablero.colocar_ficha(0, 0, "X")
        resultado = self.tablero.colocar_ficha(0, 0, "O")
        self.assertFalse(resultado)
        self.assertEqual(self.tablero.casillas[0][0], "X")
    
    def test_verificar_ganador_fila(self):
        """Verifica ganador por fila completa"""
        for col in range(3):
            self.tablero.colocar_ficha(0, col, "X")
        self.assertTrue(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))
    
    def test_verificar_ganador_columna(self):
        """Verifica ganador por columna completa"""
        for fila in range(3):
            self.tablero.colocar_ficha(fila, 0, "O")
        self.assertTrue(self.tablero.verificar_ganador("O"))
        self.assertFalse(self.tablero.verificar_ganador("X"))
    
    def test_verificar_ganador_diagonal_principal(self):
        """Verifica ganador por diagonal principal"""
        for i in range(3):
            self.tablero.colocar_ficha(i, i, "X")
        self.assertTrue(self.tablero.verificar_ganador("X"))
    
    def test_verificar_ganador_diagonal_secundaria(self):
        """Verifica ganador por diagonal secundaria"""
        for i in range(3):
            self.tablero.colocar_ficha(i, 2-i, "O")
        self.assertTrue(self.tablero.verificar_ganador("O"))
    
    def test_sin_ganador(self):
        """Verifica que no hay ganador en tablero incompleto"""
        self.tablero.colocar_ficha(0, 0, "X")
        self.tablero.colocar_ficha(1, 1, "O")
        self.assertFalse(self.tablero.verificar_ganador("X"))
        self.assertFalse(self.tablero.verificar_ganador("O"))
    
    def test_tablero_vacio_no_lleno(self):
        """Verifica que tablero vacío no está lleno"""
        self.assertFalse(self.tablero.tablero_lleno())
    
    def test_tablero_parcial_no_lleno(self):
        """Verifica que tablero parcial no está lleno"""
        self.tablero.colocar_ficha(0, 0, "X")
        self.tablero.colocar_ficha(1, 1, "O")
        self.assertFalse(self.tablero.tablero_lleno())
    
    def test_tablero_lleno_completo(self):
        """Verifica tablero completamente lleno"""
        fichas = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
        pos = 0
        for fila in range(3):
            for col in range(3):
                self.tablero.colocar_ficha(fila, col, fichas[pos])
                pos += 1
        self.assertTrue(self.tablero.tablero_lleno())


if __name__ == "__main__":
    unittest.main()