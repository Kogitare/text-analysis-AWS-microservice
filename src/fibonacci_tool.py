# Functions used in fibonacci related operations

from sympy import fibonacci, sqrt, N, ln

phi = N((1 + sqrt(5))/2, 20)  # phi number for mathematical operations

def is_in_fibo(number: int) -> bool:
    """Check if number is part of the fibonacci sequence."""
    if sqrt(5 * number**2 + 4).is_integer or sqrt(5 * number**2 - 4).is_integer: return True
    else: return False

def find_fibo_id(number: int) -> int:
    """Find position of a number in fibonacci sequence."""
    pos = ln(number * sqrt(5) + 1.0/2, phi) // 1
    return pos if pos > 0 else 1

def get_fibo_num(pos: int) -> int:
    """Get fibonacci number in specific position."""
    return int(fibonacci(pos))

def get_prev_next_fibo(integer: int) -> list:
    """Create list with previous and next fibonacci number (replaced by None if not fibonacci number)."""
    if is_in_fibo(integer):
        id_in_fib = find_fibo_id(integer) - 1
        return [get_fibo_num(id_in_fib), integer, get_fibo_num(id_in_fib+2)]
    else:
        return [None, integer, None]