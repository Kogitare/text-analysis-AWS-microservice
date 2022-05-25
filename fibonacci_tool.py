# Functions used in fibonacci related operations

import math

phi = (1 + math.sqrt(5))/2

def is_in_fibo(number: int):
    check_equation = lambda sign: math.sqrt(5* number**2 +(4*sign)) - int(math.sqrt(5* number**2 +(4*sign)))
    if check_equation(1) == 0 or check_equation(-1) == 0: return True
    else: return False

def find_fibo_id(number: int):
    return int(math.log(number*math.sqrt(5) + 1.0/2, phi))

def get_fibo(number: int):
    result = int((phi**number - (-phi)**(-number)) / math.sqrt(5))
    if result < 0: return 0
    else: return result