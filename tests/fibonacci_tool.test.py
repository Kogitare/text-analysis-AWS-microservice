# times how long functions from fibonacci_tool.py take

def get_values_from_file(filename):
    """Open file and extract test values"""
    with open("test_values/"+filename, 'r') as f:
        numbers = f.read()
        numbers = [int(n) for n in numbers.split('\n')]
        return numbers

import sys
sys.path.append('../src')   # add src directory to path, to access fibonacci_tool
from fibonacci_tool import *
from timeit import timeit

def time_fibo_function(function_name: str, parameters: list):
    """Times functions using provided parameters"""
    average = 0
    print('-----------------------------------------------------')
    print(f"#### TEST FOR {function_name}(n)")
    for test_num in parameters:
        res = 1000*timeit(
            f"{function_name}(n)",
            number=iterations,
            setup=f"from fibonacci_tool import {function_name}; n={test_num}"
        )
        print("time:\t", res, f'\tms\tn = {test_num}')
        average += res
    average /= len(parameters)
    print(f"Average time:\t{average}\tms")

def time_fibo_fs(functions_to_time: dict, iterations: int):
    """Prints run time of functions provided with parameters."""
    print('#####################################################')
    for function in functions_to_time.keys():
        time_fibo_function(function, functions_to_time[function])


if __name__ == "__main__":
    fib_nums = get_values_from_file("fibonacci_numbers.txt")
    n_nums = get_values_from_file("normal_numbers.txt")
    iterations = 100

    time_fibo_fs({"get_fibo_num": n_nums}, iterations)

    n_nums.append(222232244629420445529739893461909967206666123456499764990979600)

    time_fibo_fs({"is_in_fibo": fib_nums}, iterations)
    time_fibo_fs({"is_in_fibo": n_nums}, iterations)

    time_fibo_fs({"get_prev_next_fibo": fib_nums}, iterations)
    time_fibo_fs({"get_prev_next_fibo": n_nums}, iterations)

    time_fibo_fs({"find_fibo_id": fib_nums}, iterations)
    time_fibo_fs({"find_fibo_id": n_nums}, iterations)
