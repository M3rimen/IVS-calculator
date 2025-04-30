## @file calculator.py
# @brief Calculator that evaluates mathematical expressions.
# @date 2025-04-29


import re
import math_lib as math
import gui


## @brief Function to tokenize the input expression.
# @param expr input expression
# @return generator of tokens
def tokenize(expr):
    token_spec = [
        ('NUMBER',   r"\d+(?:\.\d*)?"),      # Integer or decimal
        ('NAME',     r"[a-zA-Z_π]\w*|√|n√"), # Identifiers (sin, cos, ANS, etc.)
        ('OP',       r"\*\*|[+\-*/^(),]"),   # Operators, parentheses, comma
        ('SKIP',     r"[ \t]+"),             # Skip whitespace
        ('MISMATCH', r".")                   # Any other character = error
    ]
    tok_regex = "|".join(f"(?P<{n}>{p})" for n, p in token_spec)
    for m in re.finditer(tok_regex, expr):
        kind, val = m.lastgroup, m.group()
        if kind == 'NUMBER':
            yield ('NUMBER', int(val) if '.' not in val else float(val))
        elif kind == 'NAME':
            yield ('NAME', val)
        elif kind == 'OP':
            yield ('OP', val)
        elif kind == 'SKIP':
            continue
        else:
            raise SyntaxError(f"Unexpected character {val}")


## @brief Class to parse the tokenized input.
class Parser:

    ## @brief Constructor for the Parser class.
    # @param tokens list of tokens
    # @param last_ans last answer used in the calculator
    def __init__(self, tokens, last_ans=0):
        self.tokens = tokens
        self.pos = 0
        self.last_ans = last_ans
        


    ## @brief Function to get the current token.
    # @return current token
    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF','')


    ## @brief Function to advance to the next token.
    # @details Increments the position of the current token.
    def advance(self):
        self.pos += 1


    ## @brief Function to parse the expression.
    # @details Parses the entire expression and returns the abstract syntax tree (AST).
    # @return AST node representing the expression
    def parse(self):
        node = self.parse_expression()
        if self.current()[0] != 'EOF':
            raise SyntaxError("Unexpected token after end")
        return node


    ## @brief Function to parse the expression.
    # @details Handles addition and subtraction.
    # @return AST node representing the expression
    def parse_expression(self):
        node = self.parse_term()
        while self.current()[1] in ('+', '-'):
            op = self.current()[1]; self.advance()
            right = self.parse_term()
            node = ('binop', op, node, right)
        return node


    ## @brief Function to parse the term.
    # @details Handles multiplication and division.
    # @return AST node representing the term
    def parse_term(self):
        node = self.parse_power()
        while self.current()[1] in ('*', '/'):
            op = self.current()[1]; self.advance()
            right = self.parse_power()
            node = ('binop', op, node, right)
        return node


    ## @brief Function to parse power.
    # @details Handles exponentiation.
    # @return AST node representing power
    def parse_power(self):
        node = self.parse_factor()
        while self.current()[1] in ('^', '**'):
            op = self.current()[1]; self.advance()
            right = self.parse_power()
            node = ('binop', op, node, right)
        return node


    ## @brief Function to parse the factor.
    # @details Handles parentheses, numbers, identifiers, and unary minus.
    # @return AST node representing the factor
    def parse_factor(self):
        typ, val = self.current()

        # Parentheses
        if val == '(':
            self.advance()
            node = self.parse_expression()
            if self.current()[1] != ')':
                raise SyntaxError("Missing ')'")
            self.advance()
            return node

        # Number literal
        if typ == 'NUMBER':
            self.advance()
            return ('number', val)

        # Identifier: ANS or function
        if typ == 'NAME':
            name = val
            self.advance()

            # ANS constant
            if name.upper() == 'ANS':
                return ('number', self.last_ans)
            
            # Handle constants 'e' and 'π'
            if name == 'e':
                return ('number', math.compute_e())
            if name == 'π':
                return ('number', math.pi())

            # Function call
            if self.current()[1] == '(':
                self.advance()  # consume '('
                args = []

                # Zero-argument
                if self.current()[1] == ')':
                    self.advance()
                    return ('func0', name)

                # One or more args
                args.append(self.parse_expression())
                while self.current()[1] == ',':
                    self.advance()
                    args.append(self.parse_expression())

                if self.current()[1] != ')':
                    raise SyntaxError("Missing ')' after function args")
                self.advance()

                if len(args) == 1:
                    return ('func1', name, args[0])
                if len(args) == 2:
                    return ('func2', name, args[0], args[1])
                raise SyntaxError("Too many function arguments")

            raise SyntaxError(f"Unknown identifier '{name}'")

        # Unary minus
        if val == '-':
            self.advance()
            node = self.parse_factor()
            return ('uminus', node)

        raise SyntaxError(f"Unexpected token '{val}'")


## @brief Function to evaluate the AST node.
# @param node AST node
# @param ns namespace for functions and constants
# @return evaluated value of the node
def eval_node(node, ns):
    kind = node[0]

    if kind == 'number':
        return node[1]

    if kind == 'binop':
        _, op, left, right = node
        l = eval_node(left, ns)
        r = eval_node(right, ns)
        if op in ('^','**'): return l ** r
        if op == '+':       return l + r
        if op == '-':       return l - r
        if op == '*':       return l * r
        if op == '/':       return l / r
        raise ValueError(f"Unknown operator {op}")

    if kind == 'uminus':
        return -eval_node(node[1], ns)

    if kind == 'func0':
        _, fname = node
        f = ns.get(fname.lower())
        if not f:
            raise ValueError(f"Unknown function {fname}")
        return f()

    if kind == 'func1':
        _, fname, arg = node
        f = ns.get(fname.lower())
        if not f:
            raise ValueError(f"Unknown function {fname}")
        return f(eval_node(arg, ns))

    if kind == 'func2':
        _, fname, a1, a2 = node
        f = ns.get(fname.lower())
        if not f:
            raise ValueError(f"Unknown function {fname}")
        return f(eval_node(a1, ns), eval_node(a2, ns))

    raise ValueError(f"Invalid AST node {node}")


## @brief Function to build a safe namespace for the calculator.
# @param last_ans last answer used in the calculator
# @param base base for number conversion
# @return dictionary of functions and constants
def build_safe_ns(last_ans, base=10):
    return {
        'sin':       math.sin,
        'cos':       math.cos,
        'tg':        math.tg,
        'cotg':      math.cotg,
        'ln':        math.ln,
        'log':       math.log,
        '√':         math.sqrt,
        'n√':        math.nthroot,
        'nthroot':   math.nthroot,  # ← Added alias for ASCII form
        'abs':       math.abs,
        'fact':      math.fact,
        'compute_e': math.compute_e,
        'pi':        math.pi,
    }


## @brief Function to evaluate the expression.
# @param expr input expression
# @param base base for number conversion (2, 8, or 10)
# @return evaluated result as a string
def evaluate(expr, base=10):
    last_ans = 0

    # 1) Convert base-literal → decimal
    if base != 10:
        if base == 2:
            pat, conv = r'\b[01]+\b', lambda m: str(int(m.group(), 2))
        else:
            pat, conv = r'\b[0-7]+\b', lambda m: str(int(m.group(), 8))
        expr = re.sub(pat, conv, expr)
    
    expr = expr.replace("n√", "nthroot")

    # 2)&3) Mask commas, convert decimal commas
    expr = re.sub(r'(nthroot\(\s*[^,()]+\s*),(?=\s*[^,()]+\s*\))',
                  lambda m: m.group(1) + '#', expr)
    expr = re.sub(r'(log\(\s*[^,()]+\s*),(?=\s*[^,()]+\s*\))',
                  lambda m: m.group(1) + '#', expr)
    expr = re.sub(r'(?<=\d),(?=\d)', '.', expr)
    expr = expr.replace('#', ',')
    expr = re.sub(r'n√\s*\(([^,]+),\s*([^)]+)\)', r'nthroot(\1,\2)', expr)

    try:
        tokens = list(tokenize(expr)) + [('EOF','')]
        parser = Parser(tokens, last_ans)
        ast    = parser.parse()
        ns     = build_safe_ns(last_ans, base)

        # 6) Integer division remainder in 2/8
        if base != 10 and ast[0] == 'binop' and ast[1] == '/':
            l = eval_node(ast[2], ns)
            r = eval_node(ast[3], ns)
            if r == 0:
                return "Error"
            q, rem = l // r, l % r
            if base == 2:
                return f"{bin(q)[2:]} zv.{bin(rem)[2:]}"
            else:
                return f"{oct(q)[2:]} zv.{oct(rem)[2:]}"

        # Standard eval
        result = eval_node(ast, ns)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        # 7) Convert back to chosen base / format
        if isinstance(result, int):
            if base == 2: return bin(result)[2:]
            if base == 8: return oct(result)[2:]
            return str(result)
        s = f"{round(result,10):.10f}".rstrip('0').rstrip('.')
        return s if '.' in s else s + '.0'

    except Exception:
        return "Error"

if __name__ == "__main__":
    gui.main()

# end of calculator.py