import unittest
from io import StringIO
import sys

def greet(name):
    print(f"Cześć, {name}!")

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        # Przechwycenie standardowego wyjścia
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Wywołanie funkcji
        greet("Rafał")
        
        # Przywrócenie standardowego wyjścia
        sys.stdout = sys.__stdout__
        
        # Sprawdzenie wyniku
        self.assertEqual(captured_output.getvalue().strip(), "Cześć, Rafał!")

if __name__ == "__main__":
    unittest.main()
