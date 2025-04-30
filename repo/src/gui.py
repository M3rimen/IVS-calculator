## @file gui.py
# @brief GUI for the calculator.
# @details This script creates a graphical user interface for a calculator using the Tkinter library.
# @date 2025-04-29

import tkinter as tk
from calculator import evaluate
import sys
import os

def resource_path(relative_path):
    ## @brief Resolves the resource path for bundled applications.
    # @param relative_path The relative path to the resource file.
    # @details Detects if running under PyInstaller (using _MEIPASS) and returns the appropriate absolute path.
    # @return The absolute path to the resource.
    try:
        base_path = sys._MEIPASS  # PyInstaller-specific temp path
    except AttributeError:
        base_path = os.path.abspath(".")  # Fallback to current directory
    return os.path.join(base_path, relative_path)

class CalculatorGUI:
    ## @brief Constructor for the CalculatorGUI class.
    # @param master The Tkinter root window.
    # @details Initializes window properties, state variables, layouts, buttons, display labels, and keyboard bindings.
    def __init__(self, master):
        self.master = master

        # Window properties
        master.title("LuceNext")
        master.configure(bg='black')
        master.geometry("450x650")
        icon = tk.PhotoImage(file=resource_path('icon.png'))
        master.iconphoto(True, icon)
        master.resizable(False, False)

        # Help button
        help_btn = tk.Button(master, text='?', width=3, height=1,
                             command=self.show_help, bd=0, relief='flat',
                             bg='gray25', fg='white')
        help_btn.grid(row=0, column=0, sticky='nw', padx=2, pady=2)

        # Keyboard event binding
        master.bind('<Key>', self.on_keypress)

        # Uniform column/row configuration
        for i in range(5):
            master.grid_columnconfigure(i, weight=1, uniform='col')
        for r in range(11):
            master.grid_rowconfigure(r, weight=1)

        # State variables
        self.after_equal = False
        self.expr_var = tk.StringVar()     # Holds current expression
        self.result_var = tk.StringVar()   # Holds displayed result
        self.last_result = 0               # Stores last computed numeric result

        # Display labels for expression and result
        tk.Label(master, textvariable=self.expr_var, anchor='e',
                 bg='black', fg='white', font=('Arial',20))\
          .grid(row=1, column=0, columnspan=5, sticky='we', padx=2, pady=(2,0))
        tk.Label(master, textvariable=self.result_var, anchor='e',
                 bg='black', fg='white', font=('Arial',40))\
          .grid(row=2, column=0, columnspan=5, sticky='we', padx=2, pady=(0,2))

        # Base selection radio buttons (Decimal, Octal, Binary)
        self.base_var = tk.IntVar(value=10)
        for idx, (text, val) in enumerate([('Decimal',10), ('Octal',8), ('Binary',2)]):
            rb = tk.Radiobutton(master, text=text, variable=self.base_var,
                                value=val, command=self.change_base,
                                bg='gray20', fg='white', selectcolor='gray30',
                                bd=0, highlightthickness=0, relief='flat')
            rb.grid(row=3, column=idx, sticky='nsew', padx=2, pady=2)
        tk.Label(master, bg='black').grid(row=3, column=3, columnspan=2)

        # Define button layout and styling
        btn_rows = [
            ['sin','cos','tg','cotg','e'],
            ['ln','log','|x|','CE','⌫'],
            ['ⁿ√','(',')','!','÷'],
            ['√','7','8','9','×'],
            ['x²','4','5','6','–'],
            ['xʸ','1','2','3','+'],
            ['π','ANS','0',',','=']
        ]
        self.buttons = {}  

        for r, row in enumerate(btn_rows, start=4):
            for c, char in enumerate(row):
                cmd = lambda ch=char: self.on_button(ch)
                btn = tk.Button(master, text=char, width=4, height=2,
                                command=cmd, bd=0, relief='flat',
                                highlightthickness=0)
                # Color scheme by type
                if char.isdigit() or char in (',', 'ANS'):
                    btn.config(bg='gray30', fg='white')
                elif char in ['+','–','×','÷','=']:
                    btn.config(bg='darkorange', fg='black')
                else:
                    btn.config(bg='white', fg='black')
                btn.grid(row=r, column=c, sticky='nsew', padx=2, pady=2)
                self.buttons[char] = btn

    ## @brief Opens a help window with usage instructions.
    # @details Creates a scrollable Toplevel window listing all operations, parameters, and notes.
    # @return None
    def show_help(self):
        help_win = tk.Toplevel(self.master)
        help_win.title("Calculator Help")
        help_win.geometry("700x500")
        help_win.configure(bg='black')
        help_win.resizable(False, False)

        text = tk.Text(help_win, bg='black', fg='white', font=('Arial', 11),
                       wrap=tk.WORD, padx=20, pady=20)
        scrollbar = tk.Scrollbar(help_win, command=text.yview)
        text.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.pack(expand=True, fill=tk.BOTH)

        # Define tag styles for headings and content
        text.tag_configure("title", foreground="darkorange", font=('Arial', 18, 'bold'))
        text.tag_configure("item", foreground="white", font=('Arial', 10, 'bold'))
        text.tag_configure("usage_note", foreground="gold", font=('Arial', 10, 'bold'))
        text.tag_configure("desc", foreground="white", font=('Arial', 10))

        # Content sections
        sections = [
            ("Simple Operations", [
                ("Usage", "x + y"),
                ("Note", "Not supplying parameters returns 0."),
                ("Addition (+)", "Add two numbers."),
                ("Subtraction (-)", "Subtract the second number from the first."),
                ("Multiplication (×)", "Multiply two numbers."),
                ("Division (÷)", "Divide the first number by the second.")
            ]),
            ("Operations with One Parameter", [
                ("Usage", "Function(x)"),
                ("Square Root (√)", "Calculate the square root of a number."),
                ("Factorial (!)", "Calculate the factorial of a number."),
                ("Sine (sin)", "Calculate the sine of an angle in degrees."),
                ("Cosine (cos)", "Calculate the cosine of an angle in degrees."),
                ("Tangent (tg)", "Calculate the tangent of an angle in degrees."),
                ("Natural Logarithm (ln)", "Calculate the natural logarithm of a number."),
                ("Absolute Value (|x|)", "Calculate the absolute value of a number.")
            ]),
            ("Operations with Two Parameters", [
                ("Usage", "Function(x, y)"),
                ("Logarithm (log)", "Calculate the logarithm with custom base."),
                ("Exponentiation (xʸ)", "Raise x to the power of y."),
                ("N-th Root (ⁿ√)", "Calculate the y-th root of x.")
            ]),
            ("Constants", [
                ("Euler's Number (e)", "Approximately 2.71828"),
                ("Pi (π)", "Approximately 3.14159")
            ]),
            ("System Operations", [
                ("Clear Entry (CE)", "Erase the entire current expression."),
                ("Backspace (⌫)", "Delete the last entered character."),
                ("Decimal Point (,)", "Insert a decimal separator."),
                ("ANS", "Insert last computed result."),
                ("Equals (=)", "Evaluate the expression.")
            ]),
        ]

        # Insert structured help text
        for title, items in sections:
            text.insert(tk.END, f"{title}\n", "title")
            for item, desc in items:
                if item == "Usage" or item == "Note":
                    text.insert(tk.END, f"  {item}: {desc}\n", "usage_note")
                else:
                    text.insert(tk.END, f"  {item}: ", "item")
                    text.insert(tk.END, f"{desc}\n", "desc")
            text.insert(tk.END, "\n")

        text.config(state=tk.DISABLED)

    ## @brief Handles keyboard input mapping.
    # @param event The Tkinter keyboard event.
    # @details Maps keys (digits, operators, Enter, Backspace, Delete) to corresponding button actions, validating against current base.
    # @return None
    def on_keypress(self, event):
        ch = event.char
        base = self.base_var.get()

        # Digit entry validation against base
        if ch.isdigit():
            if int(ch) >= base:
                return
            self.on_button(ch)
            return

        # Decimal point only in base 10
        if ch == '.' and base == 10:
            self.on_button(',')
            return

        # Map common operators to display symbols
        if ch in '+-*/':
            disp = {'*': '×', '/': '÷', '+': '+', '-': '–'}[ch]
            self.on_button(disp)
            return

        # Exponentiation key
        if ch == '^':
            self.on_button('xʸ')
            return

        # Enter key for equals
        if ch == '=' or event.keysym == 'Return':
            self.on_button('=')
            return

        # Backspace and Delete
        if event.keysym == 'BackSpace':
            self.on_button('⌫')
            return
        if event.keysym == 'Delete':
            self.on_button('CE')
            return

    ## @brief Processes button presses from UI or keyboard.
    # @param char The label of the button pressed.
    # @details Handles insertion of characters/functions, evaluation on '=', clear/backspace, ANS insertion, and state resets.
    # @return None
    def on_button(self, char):
        expr = self.expr_var.get()
        # Prevent stacking multiple functions without operands
        block_funcs = ['sin','cos','tg','cotg','ln','log','|x|','√','ⁿ√','!','e','π']
        if expr and char in block_funcs:
            return

        # Handle ANS insertion
        if char == 'ANS':
            ans = self.last_result
            base = self.base_var.get()
            if base in (2, 8) and isinstance(ans, (int, float)):
                ans = int(ans)
            ans_str = self.format_result(ans).replace('.', ',')
            if self.after_equal or not expr:
                self.expr_var.set(ans_str)
            else:
                self.expr_var.set(expr + ans_str)
            self.after_equal = False
            return

        # Clear Entry
        if char == 'CE':
            self.expr_var.set("")
            self.result_var.set("")
            self.after_equal = False
            self.change_base()
            return

        # Backspace
        if char == '⌫':
            self.expr_var.set(expr[:-1])
            return

        # Evaluate expression
        if char == '=':
            # Auto-close parentheses
            open_p = expr.count('(')
            close_p = expr.count(')')
            if open_p > close_p:
                expr += ')' * (open_p - close_p)
                self.expr_var.set(expr)
            result = evaluate(expr, self.base_var.get())
            self.last_result = result
            out = self.format_result(result).replace('.', ',')
            self.result_var.set(out)
            self.after_equal = True
            # Disable buttons on error except CE
            if out == "Error":
                for ch2, btn in self.buttons.items():
                    if ch2 != 'CE':
                        btn.config(state='disabled')
            return

        # Reset state if new input after '='
        if self.after_equal:
            if char.isdigit() or char == ',':
                new_expr = char
            else:
                new_expr = self.format_result(self.last_result) + self._get_mapping().get(char, char)
            self.expr_var.set(new_expr)
            self.result_var.set("")
            self.after_equal = False
            return

        # Prevent invalid operator sequences
        mapped = self._get_mapping().get(char, char)
        if mapped in ['+', '-', '*', '/']:
            if not expr or expr[-1] in ['+', '-', '*', '/']:
                if mapped == '-' and not expr:
                    self.expr_var.set('-')
                return

        # Append mapped character
        self.expr_var.set(expr + mapped)

    ## @brief Provides mapping from display symbols to evaluation tokens.
    # @details Returns a dictionary mapping button labels (e.g., '×','sin') to the corresponding expression strings for the evaluator.
    # @return A dict mapping UI labels to evaluator tokens.
    def _get_mapping(self):
        return {
            '×':'*', '÷':'/', '–':'-',
            'x²':'^2', 'xʸ':'^(',
            '√':'√(', 'ⁿ√':'n√(',
            '(':'(', ')':')',
            '!':'fact(', 'sin':'sin(', 'cos':'cos(',
            'tg':'tg(', 'cotg':'cotg(', 'ln':'ln(',
            'log':'log(', '|x|':'abs(', 'e':'e',
            'π':'π', 'ANS':'ANS'
        }

    ## @brief Formats numeric results according to selected base and type.
    # @param res The result to format (int or float).
    # @details Converts ints to binary/octal/decimal strings, floats to fixed precision (10 decimals, trimmed).
    # @return A string representation of the result.
    def format_result(self, res):
        if isinstance(res, int):
            base = self.base_var.get()
            if base == 2:
                return bin(res)[2:]
            if base == 8:
                return oct(res)[2:]
            return str(res)
        if isinstance(res, float):
            rounded = round(res, 10)
            s = f"{rounded:.10f}".rstrip('0').rstrip('.')
            if '.' not in s:
                s += '.0'
            if s == "-0.0":
                s = "0.0"
            return s
        return str(res)

    ## @brief Enables/disables calculator buttons based on current base.
    # @details Activates only valid digit buttons for binary/octal, always enables operators and control keys, and resets display.
    # @return None
    def change_base(self):
        base = self.base_var.get()
        if base == 10:
            for btn in self.buttons.values():
                btn.config(state='normal')
        else:
            for ch, btn in self.buttons.items():
                if ch.isdigit():
                    btn.config(state='normal' if int(ch) < base else 'disabled')
                elif ch in ['+','–','×','÷','=','ANS','CE','⌫','(',')']:
                    btn.config(state='normal')
                else:
                    btn.config(state='disabled')
        # Update operator button colors by base
        color = 'darkorange' if base == 10 else 'yellow' if base == 8 else 'cyan'
        for op in ['+','–','×','÷','=']:
            self.buttons[op].config(bg=color)
        # Reset expression and result
        self.expr_var.set("")
        self.result_var.set("")
        self.after_equal = False

## @brief Main entry point launching the calculator GUI.
# @details Initializes the Tk root window, sets minimum and maximum sizes, and starts the main event loop.
# @return None
def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.update_idletasks()
    w, h = root.winfo_width(), root.winfo_height()
    root.minsize(w, h)
    root.maxsize(w, h)
    root.mainloop()

if __name__ == '__main__':
    main()
