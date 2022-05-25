# Text analysis functions

import re
import fibonacci_tool

def get_integers(text: str):
    matches = list(set([int(num) for num in re.findall(r'[0-9]+', text)]))
    matches.sort()
    return matches

def get_fibonacci(int_list: list):
    for integer, i in zip(int_list, range(len(int_list))):
        if fibonacci_tool.is_in_fibo(integer):
            fib_sequence = []
            id_in_fib = fibonacci_tool.find_fibo_id(integer) - 1
            fib_sequence.append(fibonacci_tool.get_fibo(id_in_fib))
            fib_sequence.append(integer)
            fib_sequence.append(fibonacci_tool.get_fibo(id_in_fib+2))
            int_list[i] = fib_sequence
        else:
            int_list[i] = [None, integer, None]
    return int_list
            

def get_words(text: str):
    matches = [num.lower() for num in re.findall(r'[a-zA-Z]+', text)]
    unique_matches = list(set(matches))
    words = {}
    for match in unique_matches:
        words[match] = matches.count(match)
    return words