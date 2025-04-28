import tkinter as tk
from calculator import evaluate

class CalculatorGUI:
    def __init__(self, master):
        self.master = master

        master.title("LuceNext")
        master.configure(bg='black')
        master.geometry("450x650")
        icon = tk.PhotoImage(file='src/icon.png')
        master.iconphoto(True, icon)
        master.resizable(False, False)

        # Add help button at top-left
        help_btn = tk.Button(
            master, text='?', width=3, height=1,
            command=self.show_help, bd=0, relief='flat',
            highlightthickness=0, bg='gray30', fg='white'
        )
        help_btn.grid(row=0, column=0, sticky='nw', padx=2, pady=2)

        for i in range(5):
            master.grid_columnconfigure(i, weight=1, uniform='col')
        for r in range(0, 11):
            master.grid_rowconfigure(r, weight=1)

        self.after_equal = False
        self.expr_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.last_result = 0

        tk.Label(master, textvariable=self.expr_var,
                 anchor='e', bg='black', fg='white',
                 font=('Arial', 20)) \
          .grid(row=1, column=0, columnspan=5,
                sticky='we', padx=2, pady=(2,0))
        tk.Label(master, textvariable=self.result_var,
                 anchor='e', bg='black', fg='white',
                 font=('Arial', 40)) \
          .grid(row=2, column=0, columnspan=5,
                sticky='we', padx=2, pady=(0,2))

        self.base_var = tk.IntVar(value=10)
        for idx, (text, val) in enumerate([('Decimal',10),
                                           ('Octal',8),
                                           ('Binary',2)]):
            rb = tk.Radiobutton(
                master, text=text, variable=self.base_var, value=val,
                command=self.change_base, bg='gray20', fg='white',
                selectcolor='gray30', bd=0, highlightthickness=0,
                relief='flat'
            )
            rb.grid(row=3, column=idx, sticky='nsew', padx=2, pady=2)

        tk.Label(master, bg='black') \
          .grid(row=3, column=3, columnspan=2)

        btn_rows = [
            ['sin','cos','tg','cotg','e'],
            ['ln','log','|x|','CE','⌫'],
            ['√','³√','ⁿ√','!','÷'],
            ['x²','7','8','9','×'],
            ['x³','4','5','6','–'],
            ['xʸ','1','2','3','+'],
            ['π','ANS','0',',','=' ]
        ]

        self.buttons = {}
        for r, row in enumerate(btn_rows, start=4):
            for c, char in enumerate(row):
                cmd = lambda ch=char: self.on_button(ch)
                btn = tk.Button(
                    master, text=char, width=4, height=2,
                    command=cmd, bd=0, relief='flat',
                    highlightthickness=0
                )
                if char.isdigit() or char in (',', 'ANS'):
                    btn.config(bg='gray30', fg='white')
                elif char in ['+','–','×','÷','=']:
                    btn.config(bg='darkorange', fg='black')
                else:
                    btn.config(bg='white', fg='black')
                btn.grid(row=r, column=c, sticky='nsew', padx=2, pady=2)
                self.buttons[char] = btn

    def show_help(self):
            help_win = tk.Toplevel(self.master)
            help_win.title("Calculator Help")
            help_win.geometry("700x500")
            help_win.configure(bg='black')
            help_win.resizable(False, False)

            # Text widget with scrollbar 
            text = tk.Text(
                help_win, 
                bg='black', 
                fg='white', 
                font=('Arial', 11), 
                wrap=tk.WORD, 
                padx=20, 
                pady=20
            )
            scrollbar = tk.Scrollbar(help_win, command=text.yview)
            text.configure(yscrollcommand=scrollbar.set)

            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            text.pack(expand=True, fill=tk.BOTH)

            # Configure tags for styling
            text.tag_configure("title", foreground="cyan", font=('Arial', 14, 'bold'))
            text.tag_configure("item", foreground="white", font=('Arial', 10, 'bold'))
            text.tag_configure("usage_note", foreground="yellow")
            text.tag_configure("desc", foreground="white")

            # Content of the help message
            sections = [
                ("Simple Operations", [
                    ("Usage", "x + y"),
                    ("Note", "Not supplying parameters returns 0."),
                    ("Note", "First parameter [x] not mandatory for addition/subtraction."),
                    ("Addition (+)", "Add two numbers."),
                    ("Subtraction (-)", "Subtract the second number from the first."),
                    ("Multiplication (×)", "Multiply two numbers."),
                    ("Division (÷)", "Divide the first number by the second.")
                ]),
                ("Operations with One Parameter", [
                    ("Usage", "Function(x)"),
                    ("Note", "More or less than 1 parameter returns 0."),
                    ("Square Root (√)", "Calculate the square root of a number."),
                    ("Cube Root (³√)", "Calculate the cube root of a number."),
                    ("Factorial (!)", "Calculate the factorial of a number."),
                    ("Square (x²)", "Raise a number to the power of 2."),
                    ("Cube (x³)", "Raise a number to the power of 3."),
                    ("Sine (sin)", "Calculate the sine of an angle in degrees."),
                    ("Cosine (cos)", "Calculate the cosine of an angle in degrees."),
                    ("Tangent (tan)", "Calculate the tangent of an angle in degrees."),
                    ("Cotangent (cot)", "Calculate the cotangent of an angle in degrees."),
                    ("Natural Logarithm (ln)", "Calculate the natural logarithm of a number."),
                    ("Absolute Value (|x|)", "Calculate the absolute value of a number.")
                ]),
                ("Operations with Two Parameters", [
                    ("Usage", "Function(x, y)"),
                    ("Note", "More or less than 2 parameters returns 0."),
                    ("Logarithm (log)", "Calculate the logarithm of a number with base y."),
                    ("N-th Root (ⁿ√)", "Calculate the n-th root of a number (y-th root of x)."),
                    ("Exponentiation (xʸ)", "Raise x to the power of y.")
                ]),
                ("Constants", [
                    ("Euler's Number (e)", "Approximately 2.71828"),
                    ("Pi (π)", "Approximately 3.14159")
                ]),
                ("System Operations", [
                    ("Clear Entry (CE)", "Erase the last number entered."),
                    ("Backspace (⌫)", "Delete the last digit entered."),
                    ("Decimal Point (,)", "Insert a decimal separator."),
                    ("Equals (=)", "Compute and show the result.")
                ]),
                ("Notes", [
                    ("General", "Enter numbers and operations in natural sequence."),
                    ("ANS", "ANS works between number bases.")
                ])
            ]

            for title, items in sections:
                text.insert(tk.END, f"{title}\n", "title")
                for item, desc in items:
                    if item.startswith(("Usage", "Note")):
                        text.insert(tk.END, f"  {item}: {desc}\n", "usage_note")
                    else:
                        text.insert(tk.END, f"  {item}: ", "item")
                        text.insert(tk.END, f"{desc}\n", "desc")
                text.insert(tk.END, "\n")

            text.config(state=tk.DISABLED)  # Make read-only
            

    def on_button(self, char):
        expr = self.expr_var.get()

        if char == 'ANS':
            ans_str = self.format_result(self.last_result).replace('.', ',')
            if self.after_equal or not expr:
                self.expr_var.set(ans_str)
            else:
                self.expr_var.set(expr + ans_str)
            self.after_equal = False
            return

        if char == 'CE':
            self.expr_var.set("")
            self.result_var.set("")
            self.after_equal = False
            return

        if char == '⌫':
            self.expr_var.set(expr[:-1])
            return

        if char == '=':
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
            return

        if self.after_equal:
            if char.isdigit() or char == ',':
                new_expr = char
            else:
                m = self._get_mapping()
                new_expr = self.format_result(self.last_result) + m.get(char, char)
            self.expr_var.set(new_expr)
            self.result_var.set("")
            self.after_equal = False
            return

        mapping = self._get_mapping()
        self.expr_var.set(expr + mapping.get(char, char))

    def _get_mapping(self):
        return {
            '×':'*', '÷':'/', '–':'-',
            'x²':'**2', 'x³':'**3', 'xʸ':'**',
            '√':'sqrt(', '³√':'cbrt(', 'ⁿ√':'nthroot(',
            '!':'fact(', 'sin':'sin(', 'cos':'cos(',
            'tg':'tg(', 'cotg':'cotg(', 'ln':'ln(',
            'log':'log(', '|x|':'abs(', 'ANS':'ANS',
            'e':'compute_e()', 'π':'pi()',
        }

    def format_result(self, res):
        # integer → base conversion
        if isinstance(res, int):
            base = self.base_var.get()
            if base == 2:
                return bin(res)[2:]
            if base == 8:
                return oct(res)[2:]
            return str(res)

        # float → round + strip noise, ensure at least one decimal place
        if isinstance(res, float):
            rounded = round(res, 10)
            s = f"{rounded:.10f}".rstrip('0').rstrip('.')
            if '.' not in s:
                s += '.0'
            return s

        # fallback
        return str(res)

    def change_base(self):
        base = self.base_var.get()
        for d in range(10):
            btn = self.buttons.get(str(d))
            if btn:
                btn.config(state='normal' if d < base else 'disabled')
        self.expr_var.set("")
        self.result_var.set("")

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
