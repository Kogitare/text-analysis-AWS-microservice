# Checks performance of text_analysis.py

import os, sys
from timeit import timeit
from perf_test_functions import get_string_from_file, time_function
sys.path.append('../src')   # add src directory to path
from text_analysis import *

def time_number_analysis(f: str, path: str, iterations: int):
    file_content = get_string_from_file(path+f)
    par = {'name': f, 'value': file_content}
    print(f"INPUT_AMOUNT:\t{len(get_integers(file_content))}")
    time_function("text_analysis", "get_integers", par, iterations)

def time_number_table(f: str, path: str, iterations: int):
    integers = get_integers(get_string_from_file(path+f))
    par = {'name': f, 'value': integers}
    print(f"INPUT_AMOUNT:\t{len(integers)}")
    time_function("text_analysis", "create_fibo_table", par, iterations)

def time_word_analysis(f: str, path: str, iterations: int):
    file_content = get_string_from_file(path+f)
    par = {'name': f, 'value': file_content}
    print(f"INPUT_AMOUNT:\t{len(get_words(file_content))}")
    time_function("text_analysis", "get_words", par, iterations)

if __name__ == '__main__':
    script_name = "text_analysis"
    iterations = 1

    path = "test_files/numbers/"
    directory = os.listdir(path)
    try: directory.pop(directory.index('.DS_Store'))
    except: pass
    print(path)
    print(directory)
    print("---------------------------------------------------------------")
    fun_name = "get_integers"
    for f_name in directory:
        print(f"Function {fun_name}({f_name}) from {script_name} after {iterations} iteration(s) took:")
        time_number_analysis(f_name, path, iterations)
    print("---------------------------------------------------------------")
    fun_name = "create_fibo_table"
    for f_name in directory:
        print(f"Function {fun_name}({f_name}) from {script_name} after {iterations} iteration(s) took:")
        time_number_table(f_name, path, iterations)
    
    print('\n\n')
    
    fun_name = "get_words"
    path = "test_files/words/"
    directory = os.listdir(path)
    try: directory.pop(directory.index('.DS_Store'))
    except: pass
    print(path)
    print(directory)
    print("---------------------------------------------------------------")
    for f_name in directory:
        print(f"Function {fun_name}({f_name}) from {script_name} after {iterations} iteration(s) took:")
        time_word_analysis(f_name, path, iterations)