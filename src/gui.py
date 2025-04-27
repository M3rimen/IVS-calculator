import tkinter as tk
from .logic import evaluate

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg='black')
        master.resizable(False, False)  # Lock window size

        self.after_equal = False
        self.expr_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.last_result = 0

        # Displays
        tk.Label(master, textvariable=self.expr_var,
                 anchor='e', bg='black', fg='white', font=('Arial', 14)) \
          .grid(row=0, column=0, columnspan=5, sticky='we', padx=5, pady=(5,0))
        tk.Label(master, textvariable=self.result_var,
                 anchor='e', bg='black', fg='white', font=('Arial', 24)) \
          .grid(row=1, column=0, columnspan=5, sticky='we', padx=5, pady=(0,5))

        # Base selection
        self.base_var = tk.IntVar(value=10)
        for idx, (text, val) in enumerate([("Decimal",10),("Octal",8),("Binary",2)]):
            tk.Radiobutton(master, text=text, variable=self.base_var, value=val,
                           command=self.change_base, bg='gray20', fg='white',
                           selectcolor='gray30') \
              .grid(row=2, column=idx, sticky='we', padx=2, pady=2)
        tk.Label(master, bg='black').grid(row=2, column=3, columnspan=2)  # spacer

        # Button layout
        btn_rows = [
            ['sin','cos','tg','cotg','e'],
            ['ln','log','|x|','CE','⌫'],
            ['√','³√','ⁿ√','!','÷'],
            ['x²','7','8','9','×'],
            ['x³','4','5','6','–'],
            ['xʸ','1','2','3','+'],
            ['π','ANS','0',',','=' ]   # comma instead of dot
        ]
        self.buttons = {}
        for r, row in enumerate(btn_rows, start=3):
            for c, char in enumerate(row):
                cmd = lambda ch=char: self.on_button(ch)
                btn = tk.Button(master, text=char, width=5, height=2, command=cmd)
                if char.isdigit() or char in (',', 'ANS'):
                    btn.config(bg='gray30', fg='white')
                elif char in ['+','–','×','÷','=']:
                    btn.config(bg='gold', fg='black')
                else:
                    btn.config(bg='white', fg='black')
                btn.grid(row=r, column=c, padx=2, pady=2)
                self.buttons[char] = btn

    def on_button(self, char):
        expr = self.expr_var.get()

        # 0) CE always clears everything
        if char == 'CE':
            self.expr_var.set("")
            self.result_var.set("")
            self.after_equal = False
            return

        # 1) Backspace
        if char == '⌫':
            self.expr_var.set(expr[:-1])
            return

        # 2) Equals → before eval, auto-close parentheses
        if char == '=':
            # count unclosed '('
            open_p = expr.count('(')
            close_p = expr.count(')')
            if open_p > close_p:
                expr = expr + ')' * (open_p - close_p)
                self.expr_var.set(expr)   # show the added ')' in the display

            result = evaluate(expr)
            self.last_result = result
            # convert dot→comma in output
            out = self.format_result(result).replace('.', ',')
            self.result_var.set(out)
            self.after_equal = True
            return

        # 3) After '=': either start fresh on digit/comma/ANS, or prepend last_result+op
        if self.after_equal:
            if char.isdigit() or char == ',' or char == 'ANS':
                new_expr = char
            else:
                m = self._get_mapping()
                to_add = m.get(char, char)
                new_expr = str(self.last_result).replace('.', ',') + to_add
            self.expr_var.set(new_expr)
            self.result_var.set("")
            self.after_equal = False
            return

        # 4) Normal button: append mapped text
        mapping = self._get_mapping()
        to_add = mapping.get(char, char)
        self.expr_var.set(expr + to_add)

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
        try:
            ival = int(res)
            base = self.base_var.get()
            if base == 2:
                return bin(ival)[2:]
            if base == 8:
                return oct(ival)[2:]
        except Exception:
            pass
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
    root.mainloop()
