import unittest
from unittest.mock import patch
import io
import sys
from src.cli import pedir_posicion, mostrar_mensaje


class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2'])
    def test_pedir_posicion_entrada_valida(self, mock_input):
        """Test entrada válida de fila y columna"""
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 2)

    @patch('builtins.input', side_effect=['0', '0'])
    def test_pedir_posicion_limites_validos(self, mock_input):
        """Test valores límite válidos (0,0)"""
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 0)
        self.assertEqual(columna, 0)

    @patch('builtins.input', side_effect=['2', '2'])
    def test_pedir_posicion_limites_superiores(self, mock_input):
        """Test valores límite superiores (2,2)"""
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 2)
        self.assertEqual(columna, 2)

    @patch('builtins.input', side_effect=['q'])
    def test_pedir_posicion_salir_q(self, mock_input):
        """Test salir con 'q' en fila"""
        fila, columna = pedir_posicion()
        self.assertIsNone(fila)
        self.assertIsNone(columna)

    @patch('builtins.input', side_effect=['1', 'salir'])
    def test_pedir_posicion_salir_palabra(self, mock_input):
        """Test salir con 'salir' en columna"""
        fila, columna = pedir_posicion()
        self.assertIsNone(fila)
        self.assertIsNone(columna)

    @patch('builtins.input', side_effect=[' 1 ', ' 2 '])
    def test_pedir_posicion_espacios_blancos(self, mock_input):
        """Test entrada con espacios en blanco"""
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 2)

    @patch('builtins.input', side_effect=['3', '1', '1', '1'])
    @patch('builtins.print')
    def test_pedir_posicion_fila_fuera_rango(self, mock_print, mock_input):
        """Test fila fuera de rango, luego entrada válida"""
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 1)
        mock_print.assert_called_with("Fila y columna deben estar entre 0 y 2.")

    @patch('builtins.input', side_effect=['1', '-1', '1', '1'])
    @patch('builtins.print')
    def test_pedir_posicion_columna_negativa(self, mock_print, mock_input):
        """Test columna negativa, luego entrada válida"""
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 1)
        mock_print.assert_called_with("Fila y columna deben estar entre 0 y 2.")

    @patch('builtins.input', side_effect=['abc', '1', '1'])
    @patch('builtins.print')
    def test_pedir_posicion_entrada_invalida(self, mock_print, mock_input):
        """Test entrada no numérica, luego entrada válida"""
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 1)
        mock_print.assert_called_with("Por favor ingrese números válidos o 'q' para salir.")

    @patch('builtins.input', side_effect=['1', '2.5', '1', '1'])
    @patch('builtins.print')
    def test_pedir_posicion_float_invalido(self, mock_print, mock_input):
        """Test entrada con decimal, luego entrada válida"""
        fila, columna = pedir_posicion()
        self.assertEqual(fila, 1)
        self.assertEqual(columna, 1)
        mock_print.assert_called_with("Por favor ingrese números válidos o 'q' para salir.")

    def test_mostrar_mensaje(self):
        """Test función mostrar_mensaje"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        mostrar_mensaje("Mensaje de prueba")
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Mensaje de prueba")

    def test_mostrar_mensaje_vacio(self):
        """Test mostrar mensaje vacío"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        mostrar_mensaje("")
        
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "")


if __name__ == '__main__':
    unittest.main()