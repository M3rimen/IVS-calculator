import unittest
from unittest.mock import patch
import tkinter as tk
from gui import CalculatorGUI

class TestCalculatorGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = CalculatorGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_append_digit_decimal(self):
        self.app.calc.set_mode(10)
        self.app.append_digit('5')
        self.assertEqual(self.app.current_input, '5')
        self.assertEqual(self.app.display.get(), '5')
        print("test_append_digit_decimal passed")

    def test_append_digit_binary_invalid(self):
        self.app.calc.set_mode(2)
        self.app.append_digit('2')
        self.assertEqual(self.app.current_input, '')
        self.assertEqual(self.app.display.get(), '')
        print("test_append_digit_binary_invalid passed")

    def test_clear(self):
        self.app.current_input = '123'
        self.app.expression = '1+2'
        self.app.display.insert(0, 'something')
        self.app.clear()
        self.assertEqual(self.app.current_input, '')
        self.assertEqual(self.app.expression, '')
        self.assertEqual(self.app.display.get(), '')
        print("test_clear passed")

    def test_change_mode(self):
        self.app.base_var.set('Binary')
        with patch.object(self.app, 'clear') as mock_clear:
            self.app.change_mode(None)
            mock_clear.assert_called_once()
        self.assertEqual(self.app.calc.mode, 2)
        print("test_change_mode passed")

    def test_binary_operator(self):
        self.app.current_input = '5'
        with patch.object(self.app.calc, 'input_number') as mock_input_number, \
             patch.object(self.app.calc, 'set_operator') as mock_set_operator:
            mock_input_number.return_value = 5
            self.app.binary_operator('+')
            mock_input_number.assert_called_with('5')
            mock_set_operator.assert_called_with('+')
            self.assertEqual(self.app.current_input, '')
        print("test_binary_operator passed")

    def test_equals_success(self):
        self.app.current_input = '5'
        self.app.calc.pending_operator = '+'
        with patch.object(self.app.calc, 'input_number', return_value=10), \
             patch.object(self.app.calc, 'convert_from_decimal', return_value='10'):
            self.app.expression = '5+'
            self.app.equals()
            self.assertIn('=', self.app.display.get())
            self.assertEqual(self.app.expression, '10')
            self.assertTrue(self.app.just_evaluated)
        print("test_equals_success passed")

    def test_equals_no_operator(self):
        self.app.current_input = '5'
        self.app.calc.pending_operator = None
        self.app.expression = '5+'
        self.app.equals()
        self.assertEqual(self.app.display.get(), '5+5')
        print("test_equals_no_operator passed")

    def test_unary_function_sqrt(self):
        self.app.current_input = '9'
        with patch.object(self.app.calc, 'convert_to_decimal', return_value=9), \
             patch.object(self.app.calc, 'sqrt', return_value=3), \
             patch.object(self.app.calc, 'convert_from_decimal', return_value='3'):
            self.app.unary_function('sqrt')
            self.assertIn('=', self.app.display.get())
            self.assertEqual(self.app.expression, '3')
        print("test_unary_function_sqrt passed")

    def test_unary_function_pi(self):
        self.app.current_input = ''
        self.app.calc.memory = 3.1415
        with patch.object(self.app.calc, 'convert_from_decimal', return_value='3.1415'):
            self.app.unary_function('pi')
            self.assertIn('π', self.app.display.get())
            self.assertEqual(self.app.expression, '3.1415')
        print("test_unary_function_pi passed")

if __name__ == "__main__":
    unittest.main(verbosity=2)
