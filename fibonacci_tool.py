# Functions used in fibonacci related operations

from sympy import fibonacci, sqrt, N, ln

phi = N((1 + sqrt(5))/2, 20)  # phi number for mathematical operations

def is_in_fibo(number: int) -> bool:
    """Check if number is part of the fibonacci sequence."""
    test_equation = lambda sign: sqrt(5 * number**2 +(4 * sign)) - int(sqrt(5 * number**2 +(4 * sign)))
    if test_equation(1) == 0 or test_equation(-1) == 0: return True
    else: return False

def find_fibo_id(number: int) -> int:
    """Find position of a number in fibonacci sequence."""
    return int(ln(number * sqrt(5) + 1.0/2, phi))

def get_fibo(pos: int) -> int:
    """Get fibonacci number in specific position."""
    return fibonacci(pos)