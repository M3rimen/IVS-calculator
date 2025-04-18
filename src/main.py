# main.py
from gui import CalculatorGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
