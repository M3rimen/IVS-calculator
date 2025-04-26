# calculator.py
import math_lib as math

class Calculator:
    def __init__(self, mode=10):
        """
        mode: numeral system mode (2 for binary, 8 for octal, 10 for decimal).
        memory: last computed result stored in decimal.
        pending_operator: holds a binary operator that awaits a second operand.
        """
        self.mode = mode
        self.memory = None
        self.pending_operator = None

    def set_mode(self, mode):
        """Update the numeral system mode."""
        self.mode = mode

    def convert_to_decimal(self, num_str):
        """Convert a string input (in current mode) into a decimal integer."""
        try:
            if self.mode == 10:
                return int(num_str, 10)
            elif self.mode == 2:
                return int(num_str, 2)
            elif self.mode == 8:
                return int(num_str, 8)
            else:
                return int(num_str, 10)
        except ValueError:
            raise ValueError("Invalid number for the current numeral system.")

    def convert_from_decimal(self, number):
        """Convert a decimal integer into a string in the current numeral system."""
        if self.mode == 10:
            return str(number)
        elif self.mode == 2:
            # Use built-in conversion for binary. Slice off the '0b' prefix.
            return bin(number)[2:]
        elif self.mode == 8:
            # Use built-in conversion for octal. Slice off the '0o' prefix.
            return oct(number)[2:]
        else:
            return str(number)

    # --------------------------
    # Basic binary operations
    # --------------------------
    def add(self, a, b):
        return math.add(a, b)

    def sub(self, a, b):
        return math.sub(a, b)

    def mul(self, a, b):
        return math.mul(a, b)

    def div(self, a, b):
        return math.div(a, b)

    def mod(self, a, b):
        return math.mod(a, b)

    def power(self, a, b):
        return math.power(a, b)

    def log(self, a, b):
        return math.log(a, b)

    # --------------------------
    # Unary operations
    # --------------------------
    def fact(self, a):
        return math.fact(a)

    def sqrt(self, a):
        return math.sqrt(a)

    def cbrt(self, a):
        return math.cbrt(a)

    def ln(self, a):
        return math.ln(a)

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)

    def tg(self, a):
        return math.tg(a)

    def cotg(self, a):
        return math.cotg(a)

    def pi(self):
        return math.pi()

    def e(self):
        return math.compute_e()

    # --------------------------
    # Handling input and operations
    # --------------------------
    def input_number(self, num_str):
        """
        Process an entered number (as string in the current numeral system)
        converting it to decimal. If there is a pending operator from a previous entry,
        combine that with the memory. Otherwise, store it as memory.
        """
        value = self.convert_to_decimal(num_str)
        if self.memory is None:
            self.memory = value
        else:
            if self.pending_operator is not None:
                self.memory = self.execute_operation(self.pending_operator, self.memory, value)
                self.pending_operator = None
        return self.memory

    def set_operator(self, operator):
        """Store a binary operator until the next number is input."""
        self.pending_operator = operator

    def execute_operation(self, operator, a, b):
        """Execute a binary operation given an operator and two operands (in decimal)."""
        if operator == "+":
            return self.add(a, b)
        elif operator == "-":
            return self.sub(a, b)
        elif operator == "*":
            return self.mul(a, b)
        elif operator == "/":
            return self.div(a, b)
        elif operator == "%":
            return self.mod(a, b)
        elif operator == "power":
            return self.power(a, b)
        elif operator == "log":
            return self.log(a, b)
        else:
            return None

    def clear(self):
        """Clear stored memory and pending operator."""
        self.memory = None
        self.pending_operator = None
