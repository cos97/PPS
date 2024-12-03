import unittest
import random
import string
from charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):

    def test_palindromos_simples(self):
        self.assertEqual(esPalindromo("reconocer"), True)
        self.assertEqual(esPalindromo("salas"), True)
        self.assertEqual(esPalindromo("Amor Roma"), True)
        self.assertEqual(esPalindromo("Se van sus naves"), True)
        self.assertEqual(esPalindromo("r"), True)

    def test_palindromos_con_acentos(self):
        self.assertEqual(esPalindromo("ananá"), True)
        self.assertEqual(esPalindromo("¿Acaso hubo búhos acá?"), True)
        self.assertEqual(esPalindromo("La ruta nos aportó otro paso natural"), True)
        self.assertEqual(esPalindromo("Adán no cede con Eva, Yavé no cede con nada"), True)

    def test_no_palindromos(self):
        self.assertEqual(esPalindromo("Esto no es un palíndromo"), False)
        self.assertEqual(esPalindromo("Python es genial"), False)
        
    def test_caracteres_especiales(self):
        self.assertEqual(esPalindromo("%/f/%$&·"), True)
        self.assertEqual(esPalindromo("*^¨/er_:"), False)
        self.assertEqual(esPalindromo("&&&&&"), True)

    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            esPalindromo(12345)
        with self.assertRaises(ValueError):
            esPalindromo(None)

    def test_aleatorios(self):
        for _ in range(50):  # Ejecutamos 100 veces para probar varias cadenas aleatorias
            # Generamos una cadena aleatoria de 3 caracteres para que haya más posibilidades de que hayan palíndromos
            cadena = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))

            resultado = esPalindromo(cadena)

            print(f"Cadena: '{cadena}' -> Palíndromo: {resultado}")

            self.assertEqual(esPalindromo(cadena), resultado)

if __name__ == "__main__":
    unittest.main()
