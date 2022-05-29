# Functions for performance testing

from timeit import timeit

def get_string_from_file(filepath: str):
    """Open file and get content"""
    with open(filepath, 'r') as f:
        return f.read()

units = { 'min': 1/60, 's': 1, 'ms': 1000 }
def time_function(script_name: str, fun_name: str, par: dict, iterations: int, unit='ms', silent=False):
    """Times a function using provided parameter"""
    res = timeit(
        f"{fun_name}(n)",
        number=iterations,
        setup=f"from {script_name} import {fun_name}; n={repr(par['value'])}"
    )
    if not silent: print(f"{units[unit] * res}\t{unit}")
    return res