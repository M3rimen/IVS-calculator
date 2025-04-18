# gui.py
import tkinter as tk
from tkinter import ttk
from calculator import Calculator

# Mappings for display-friendly operator symbols
BINARY_SYMBOLS = {
    "+": "+",
    "-": "-",
    "*": "×",
    "/": "÷",
    "%": "%",
    "power": "^",
    "log": " log "
}

UNARY_SYMBOLS = {
    "fact": "fact",
    "sqrt": "√",
    "cbrt": "∛",
    "ln": "ln",
    "sin": "sin",
    "cos": "cos",
    "tg": "tan",
    "cotg": "cot",
    "pi": "π",
    "e": "e"
}

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Create the Calculator logic (default in decimal)
        self.calc = Calculator(mode=10)
        
        # Expression strings and state flag
        self.expression = ""
        self.current_input = ""
        self.just_evaluated = False  # True if "=" was pressed most recently
        
        # Display widget to show current expression and result
        self.display = tk.Entry(master, font=("Arial", 16), width=40, borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
        
        # Combobox for selecting numeral system mode
        self.base_options = {"Binary": 2, "Octal": 8, "Decimal": 10}
        self.base_var = tk.StringVar(value="Decimal")
        self.base_dropdown = ttk.Combobox(master, values=list(self.base_options.keys()),
                                          textvariable=self.base_var, state="readonly", width=10)
        self.base_dropdown.grid(row=0, column=6, padx=5)
        self.base_dropdown.bind("<<ComboboxSelected>>", self.change_mode)
        
        # Create digit and operator buttons
        self.create_digit_buttons()
        self.create_operator_buttons()
        
        # Equals and Clear buttons
        self.equals_button = tk.Button(master, text="=", font=("Arial", 14), width=5, height=2, command=self.equals)
        self.equals_button.grid(row=5, column=4, padx=5, pady=5)
        
        self.clear_button = tk.Button(master, text="C", font=("Arial", 14), width=5, height=2, command=self.clear)
        self.clear_button.grid(row=5, column=5, padx=5, pady=5)

    def create_digit_buttons(self):
        digit_layout = [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['0']
        ]
        row_offset = 1
        col_offset = 0
        for r, row in enumerate(digit_layout):
            for c, digit in enumerate(row):
                btn = tk.Button(self.master, text=digit, font=("Arial", 14), width=5, height=2,
                                command=lambda d=digit: self.append_digit(d))
                btn.grid(row=row_offset + r, column=col_offset + c, padx=5, pady=5)

    def create_operator_buttons(self):
        # Binary operator buttons
        binary_ops = ["+", "-", "*", "/", "%", "power", "log"]
        row_offset = 1
        for idx, op in enumerate(binary_ops):
            btn = tk.Button(self.master, text=BINARY_SYMBOLS.get(op, op), font=("Arial", 10), width=7, height=2,
                            command=lambda oper=op: self.binary_operator(oper))
            btn.grid(row=row_offset + idx, column=3, padx=5, pady=5)
            
        # Unary function buttons
        unary_funcs = ["fact", "sqrt", "cbrt", "ln", "sin", "cos", "tg", "cotg", "pi", "e"]
        for idx, func in enumerate(unary_funcs):
            btn = tk.Button(self.master, text=UNARY_SYMBOLS.get(func, func), font=("Arial", 10), width=7, height=2,
                            command=lambda f=func: self.unary_function(f))
            btn.grid(row=1 + idx, column=6, padx=5, pady=5)

    def append_digit(self, digit):
        # Determine allowed digits based on the current numeral system
        allowed = set('0123456789')  # default for decimal
        if self.calc.mode == 2:
            allowed = set('01')
        elif self.calc.mode == 8:
            allowed = set('01234567')
        
        if digit not in allowed:
            # Ignore disallowed digits (or optionally show an error)
            return
        
        # If a new digit is typed after equals, clear out the previous result.
        if self.just_evaluated:
            self.expression = ""
            self.current_input = ""
            self.just_evaluated = False

        self.current_input += digit
        self.update_display(self.expression + self.current_input)

    def update_display(self, text):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, text)

    def clear(self):
        self.current_input = ""
        self.expression = ""
        self.calc.clear()
        self.update_display("")
        self.just_evaluated = False

    def change_mode(self, event):
        # When switching numeral systems, clear the current expression and input.
        self.clear()
        selected = self.base_var.get()
        mode = self.base_options.get(selected, 10)
        self.calc.set_mode(mode)
        print(f"Mode changed to: {selected} (base {mode})")

    def binary_operator(self, operator):
        if self.current_input:
            try:
                self.calc.input_number(self.current_input)
            except ValueError:
                self.update_display("Error")
                self.current_input = ""
                return
            op_symbol = BINARY_SYMBOLS.get(operator, operator)
            self.expression += self.current_input + op_symbol
            self.calc.set_operator(operator)
            self.current_input = ""
            self.update_display(self.expression)
            self.just_evaluated = False
        else:
            # Optionally allow replacing the operator if no new number was entered.
            pass

    def equals(self):
        if self.current_input and self.calc.pending_operator:
            try:
                result_decimal = self.calc.input_number(self.current_input)
            except ValueError:
                self.update_display("Error")
                self.current_input = ""
                return
            result_str = self.calc.convert_from_decimal(result_decimal)
            full_expr = self.expression + self.current_input + " = " + result_str
            self.update_display(full_expr)
            # Keep the result visible; set flag so that a new digit clears the answer.
            self.expression = result_str
            self.current_input = ""
            self.calc.pending_operator = None
            self.just_evaluated = True
        elif self.current_input:
            self.update_display(self.expression + self.current_input)

    def unary_function(self, func_name):
        # If no new input, then use the stored answer without clearing it.
        if not self.current_input:
            if self.calc.memory is not None:
                value = self.calc.memory
                current_str = self.calc.convert_from_decimal(value)
            else:
                self.update_display("No input")
                return
        else:
            try:
                value = self.calc.convert_to_decimal(self.current_input)
            except ValueError:
                self.update_display("Error")
                return
            current_str = self.current_input

        try:
            if func_name == "fact":
                result = self.calc.fact(value)
            elif func_name == "sqrt":
                result = self.calc.sqrt(value)
            elif func_name == "cbrt":
                result = self.calc.cbrt(value)
            elif func_name == "ln":
                result = self.calc.ln(value)
            elif func_name == "sin":
                result = self.calc.sin(value)
            elif func_name == "cos":
                result = self.calc.cos(value)
            elif func_name == "tg":
                result = self.calc.tg(value)
            elif func_name == "cotg":
                result = self.calc.cotg(value)
            elif func_name == "pi":
                result = self.calc.pi()
            elif func_name == "e":
                result = self.calc.e()
            else:
                result = value
        except Exception:
            self.update_display("Error")
            return

        symbol = UNARY_SYMBOLS.get(func_name, func_name)
        if func_name in ["pi", "e"]:
            display_expr = symbol
        else:
            display_expr = f"{symbol}({current_str})"
        self.calc.memory = result
        result_str = self.calc.convert_from_decimal(result)
        full_expr = display_expr + " = " + result_str
        # Here we update the display without clearing the answer immediately,
        # so that subsequent function operations can chain off the existing number.
        self.expression = result_str  # The result remains visible.
        self.current_input = ""
        self.update_display(full_expr)
        # Do not change 'just_evaluated' flag here so that functions chain properly.

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
