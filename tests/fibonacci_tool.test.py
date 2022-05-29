# Checks performance of fibonacci_tool.py

import os, sys
from timeit import timeit
from perf_test_functions import get_string_from_file, time_function
sys.path.append('../src')   # add src directory to path
from fibonacci_tool import *
from text_analysis import get_integers
from decimal import *

import random, turtle

def time_fibonacci_returns_int(f: str, path: str, iterations: int, function: str):
    integers = get_integers(get_string_from_file(path+f))
    if max(integers) == min(integers): print(f"INPUT:\t{max(integers)}, number_amount: {len(integers)}")
    else:
        print(f"MAX_INPUT:\t{max(integers)}, number_amount: {len(integers)}")
        print(f"MIN_INPUT:\t{min(integers)}")
    results = []
    for n in integers:
        par = {'name': f, 'value': n}
        results.append(time_function("fibonacci_tool", function, par, iterations, silent=True))
    summary = sum(results)
    results = [
        max(results),
        sum(results)/len(results),
        min(results)
    ]
    if results[0] == results[2]: print(f"{1000 * results[0]}\tms")
    else:
        print(f"SUM: {1000 * summary}   ms")
        print(f"MAX: {1000 * results[0]}   ms")
        print(f"AVG: {1000 * results[1]}   ms")
        print(f"MIN: {1000 * results[2]}   ms")

if __name__ == "__main__":
    iterations = 1
    script_name = "fibonacci_tool"

    path = "test_files/integers/"
    directory = os.listdir(path)
    try: directory.pop(directory.index('.DS_Store'))
    except: pass
    print(path)
    print(directory)
    print("---------------------------------------------------------------")
    fun_name = "is_in_fibo"
    for f_name in directory:
        print(f"Function {fun_name}({f_name}) from {script_name} after {iterations} iteration(s) took:")
        time_fibonacci_returns_int(f_name, path, iterations, fun_name)
    print("---------------------------------------------------------------")
    fun_name = "find_fibo_id"
    for f_name in directory:
        print(f"Function {fun_name}({f_name}) from {script_name} after {iterations} iteration(s) took:")
        time_fibonacci_returns_int(f_name, path, iterations, fun_name)
    print("---------------------------------------------------------------")
    fun_name = "get_prev_next_fibo"
    for f_name in directory:
        print(f"Function {fun_name}({f_name}) from {script_name} after {iterations} iteration(s) took:")
        time_fibonacci_returns_int(f_name, path, iterations, fun_name)

    path = "test_files/"
    print("---------------------------------------------------------------")
    fun_name = "find_fibo_id"
    f_name = "indexes.txt"
    print(f"Function {fun_name}({f_name}) from {script_name} after {iterations} iteration(s) took:")
    time_fibonacci_returns_int(f_name, path, iterations, fun_name)

    # time_multiplier = 350
    # origin = [-620, -370]
    # x_distance = 1

    # max_num = Decimal(10**500)
    # factor = Decimal(max_num)/Decimal(abs(origin[0])*2)
    # print(factor)

    # dots = []
    # data_point = []
    # for i in range(0, abs(origin[0])*2+1, x_distance):
    #     res = time_function("fibonacci_tool", "is_in_fibo", {'name': 'time', 'value': 10**(i+1)}, 1, silent=True)
    #     dots.append([i+origin[0], res*time_multiplier+origin[1]])
    #     data_point.append(['10^'+str(i+1), res])
    #     print(10**(i+1))
    
    # print(dots)
    # with open('points.txt', 'w') as f:
    #     f.write('\n'.join([repr(point) for point in data_point]))
    
    # numbers = get_string_from_file('logs/is_in_fibo_points.txt').split('\n')
    # numbers = [point[1:-1].split(',') for point in numbers]
    # numbers = [[point[0][:-1].split('^')[1], float(point[1])] for point in numbers]
    # numbers = [[int(point[0]), point[1]] for point in numbers]
    # numbers = [[point[0]+origin[0], point[1]*time_multiplier+origin[1]] for point in numbers]

    # turtle.tracer(False)
    # turtle.pu(); turtle.goto(origin);
    # turtle.pd(); turtle.goto(origin[0], 800)
    # turtle.pu(); turtle.goto(1000, origin[1])
    # turtle.pd(); turtle.goto(origin)
    # for i in range(30):
    #     turtle.goto(origin[0], origin[1]+i*time_multiplier); turtle.goto(abs(origin[0])*2, origin[1]+i*time_multiplier)
    #     turtle.goto(origin[0], origin[1]+i*time_multiplier)
    # turtle.update()

    # for dot in numbers:
    #     turtle.pu(); turtle.goto(dot); turtle.pd(); turtle.dot()
    # turtle.update()
    # input()

    # a = 220000
    # b = 0.02
    # numbers = [[x+origin[0], ((((x)**2)/a)+b)*time_multiplier+origin[1]] for x in range(1241)]
    # turtle.color('grey')
    # for dot in numbers:
    #     turtle.pu(); turtle.goto(dot); turtle.pd(); turtle.dot()
    # turtle.update()
    # input()