# Text analysis functions

import re   # regex library
from math import sqrt
from fibonacci_tool import get_prev_next_fibo

def get_integers(text: str) -> list:
    """Finds all integers in a string."""
    time_limit = 2
    num_limit = sqrt(180000*(time_limit-0.02))
    matches = []
    time_check = 0
    for num in re.findall(r'[0-9]+', text):
        if int(num) in matches: pass    # check if number repeats
        else: time_check += (len(num)**2)/180000 + 0.02 # uses a formula that rounds how much time it would take
        matches.append(int(num))
    matches = list(set(matches))
    if len(matches) > num_limit or time_check > time_limit: raise ValueError
    matches.sort()
    return matches

def get_words(text: str) -> dict:
    """Finds all words (and/or character sets) based on latin alphabet."""
    word_limit = 2500
    matches = [num.lower() for num in re.findall(r'[a-zA-Z]+', text)]
    unique_matches = list(set(matches))
    if len(unique_matches) > word_limit: raise ValueError
    return {match: matches.count(match) for match in unique_matches}

def create_fibo_table(integer_list: list) -> list[list]:
    """Creates a table where rows consist of integers and (if they belong) fibonacci numbers."""
    headers = ["previous Fibonacci number", "observed number", "next Fibonacci number"]
    numbers = [get_prev_next_fibo(integer) for integer in integer_list]
    table = [headers]
    table.extend(numbers)
    return table