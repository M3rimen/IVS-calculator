import re
import math_lib as math
import gui

def evaluate(expr, base=10):
    """
    1) If base≠10, convert each integer literal from that base into decimal.
    2) Preserve commas inside nthroot(...) and log(...).
    3) Convert all other numeric commas (e.g. 3,14) into dots.
    4) Restore the preserved commas.
    5) Safe eval via math_lib.
    """
    # 1) Convert integer literals from chosen base → decimal
    if base != 10:
        if base == 2:
            pat = r'\b[01]+\b'
            conv = lambda m: str(int(m.group(), 2))
        elif base == 8:
            pat = r'\b[0-7]+\b'
            conv = lambda m: str(int(m.group(), 8))
        else:
            pat = None

        if pat:
            expr = re.sub(pat, conv, expr)

    # 2) Temporarily replace argument-commas in nthroot(...) and log(...) with a placeholder '#'
    expr = re.sub(
        r'(nthroot\(\s*[^,()]+\s*),(?=\s*[^,()]+\s*\))',
        lambda m: m.group(1) + '#',
        expr
    )
    expr = re.sub(
        r'(log\(\s*[^,()]+\s*),(?=\s*[^,()]+\s*\))',
        lambda m: m.group(1) + '#',
        expr
    )

    # 3) Replace any comma between digits (decimal commas) with a dot
    expr = re.sub(r'(?<=\d),(?=\d)', '.', expr)

    # 4) Restore the argument-commas
    expr = expr.replace('#', ',')

    # 5) Build a safe namespace from math_lib
    safe_ns = {
        name: getattr(math, name)
        for name in dir(math)
        if not name.startswith('_')
    }
    safe_ns.update({
        'sqrt': math.sqrt,
        'cbrt': math.cbrt,
        'nthroot': math.nthroot,
        'fact': math.fact,
        'ln': math.ln,
        'log': math.log,
        'sin': math.sin,
        'cos': math.cos,
        'tg': math.tg,
        'cotg': math.cotg,
        'compute_e': math.compute_e,
        'pi': math.pi,
        'abs': math.abs
    })
    safe_ns['__builtins__'] = None

    try:
        return eval(expr, safe_ns, {})
    except Exception:
        return 0

if __name__ == "__main__":
    gui.main()
