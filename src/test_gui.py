import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
import pytest
from gui import CalculatorGUI  

@pytest.fixture
def app():
    root = tk.Tk()
    app = CalculatorGUI(root)
    yield app
    root.destroy()

def test_mapping(app):
    mapping = app._get_mapping()
    assert mapping['×'] == '*'
    assert mapping['÷'] == '/'
    assert mapping['x²'] == '**2'
    assert mapping['√'] == 'sqrt('
    assert mapping['π'] == 'pi()'

def test_format_result_decimal(app):
    app.base_var.set(10)
    assert app.format_result(123) == '123'
    assert app.format_result(123.456) == '123.456'

def test_format_result_binary(app):
    app.base_var.set(2)
    assert app.format_result(5) == '101'

def test_format_result_octal(app):
    app.base_var.set(8)
    assert app.format_result(9) == '11'

def test_on_button_CE_and_backspace(app):
    app.expr_var.set("12345")
    app.on_button('⌫')
    assert app.expr_var.get() == "1234"

    app.expr_var.set("987")
    app.on_button('CE')
    assert app.expr_var.get() == ""
    assert app.result_var.get() == ""

def test_change_base(app):
    app.base_var.set(2)
    app.change_base()
    # Check if digits 2-9 are disabled
    assert app.buttons['2'].cget('state') == 'disabled'
    assert app.buttons['0'].cget('state') == 'normal'

    app.base_var.set(10)
    app.change_base()
    assert app.buttons['9'].cget('state') == 'normal'
