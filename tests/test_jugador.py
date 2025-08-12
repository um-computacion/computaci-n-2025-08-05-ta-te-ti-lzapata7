import unittest
from src.jugador import Jugador


class TestJugador(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.jugador_x = Jugador("Ana", "X")
        self.jugador_o = Jugador("Luis", "O")
    
    def test_inicializacion(self):
        """Test de inicialización del jugador"""
        self.assertEqual(self.jugador_x.nombre, "Ana")
        self.assertEqual(self.jugador_x.ficha, "X")
        self.assertEqual(self.jugador_x.fichas_colocadas, 0)
        self.assertEqual(self.jugador_x.max_fichas, 3)
        
        self.assertEqual(self.jugador_o.nombre, "Luis")
        self.assertEqual(self.jugador_o.ficha, "O")
    
    def test_puede_colocar_inicial(self):
        """Test que el jugador puede colocar fichas inicialmente"""
        self.assertTrue(self.jugador_x.puede_colocar())
        self.assertTrue(self.jugador_o.puede_colocar())
    
    def test_colocar_ficha_exitoso(self):
        """Test de colocación exitosa de fichas"""
        # Primera ficha
        self.assertTrue(self.jugador_x.colocar_ficha())
        self.assertEqual(self.jugador_x.fichas_colocadas, 1)
        self.assertTrue(self.jugador_x.puede_colocar())
        
        # Segunda ficha
        self.assertTrue(self.jugador_x.colocar_ficha())
        self.assertEqual(self.jugador_x.fichas_colocadas, 2)
        self.assertTrue(self.jugador_x.puede_colocar())
        
        # Tercera ficha
        self.assertTrue(self.jugador_x.colocar_ficha())
        self.assertEqual(self.jugador_x.fichas_colocadas, 3)
        self.assertFalse(self.jugador_x.puede_colocar())
    
    def test_colocar_ficha_limite_alcanzado(self):
        """Test cuando se alcanza el límite máximo de fichas"""
        # Colocar 3 fichas
        for _ in range(3):
            self.jugador_x.colocar_ficha()
        
        # Intentar colocar una cuarta ficha
        self.assertFalse(self.jugador_x.colocar_ficha())
        self.assertEqual(self.jugador_x.fichas_colocadas, 3)
        self.assertFalse(self.jugador_x.puede_colocar())
    
    def test_puede_colocar_con_fichas_parciales(self):
        """Test de puede_colocar con diferentes cantidades de fichas"""
        # Sin fichas
        self.assertTrue(self.jugador_x.puede_colocar())
        
        # Con 1 ficha
        self.jugador_x.colocar_ficha()
        self.assertTrue(self.jugador_x.puede_colocar())
        
        # Con 2 fichas
        self.jugador_x.colocar_ficha()
        self.assertTrue(self.jugador_x.puede_colocar())
        
        # Con 3 fichas (máximo)
        self.jugador_x.colocar_ficha()
        self.assertFalse(self.jugador_x.puede_colocar())
    
    def test_diferentes_jugadores_independientes(self):
        """Test que diferentes jugadores son independientes"""
        # Jugador X coloca 2 fichas
        self.jugador_x.colocar_ficha()
        self.jugador_x.colocar_ficha()
        
        # Jugador O coloca 1 ficha
        self.jugador_o.colocar_ficha()
        
        # Verificar independencia
        self.assertEqual(self.jugador_x.fichas_colocadas, 2)
        self.assertEqual(self.jugador_o.fichas_colocadas, 1)
        self.assertTrue(self.jugador_x.puede_colocar())
        self.assertTrue(self.jugador_o.puede_colocar())


if __name__ == '__main__':
    unittest.main()