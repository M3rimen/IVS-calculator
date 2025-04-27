import re
import math_lib as math

def evaluate(expr):
    """
    1) Preserve commas inside nthroot(...) and log(...).
    2) Convert all other numeric commas (e.g. 3,14) into dots.
    3) Restore the preserved commas.
    4) Safe eval via math_lib.
    """
    # 1) Temporarily replace argument-commas in nthroot(...) and log(...) with a placeholder '#'
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

    # 2) Replace any comma between digits (decimal commas) with a dot
    expr = re.sub(r'(?<=\d),(?=\d)', '.', expr)

    # 3) Restore the argument-commas
    expr = expr.replace('#', ',')

    # 4) Prepare safe namespace from math_lib
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
