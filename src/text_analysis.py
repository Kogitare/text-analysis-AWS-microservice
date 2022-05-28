# Text analysis functions

import re   # regex library
from fibonacci_tool import get_prev_next_fibo

def get_integers(text: str) -> list:
    """Finds all integers in a string."""
    matches = list(set([int(num) for num in re.findall(r'[0-9]+', text)]))
    matches.sort()
    return matches

def get_words(text: str) -> dict:
    """Finds all words (and/or character sets) based on latin alphabet."""
    matches = [num.lower() for num in re.findall(r'[a-zA-Z]+', text)]
    unique_matches = list(set(matches))
    return {match: matches.count(match) for match in unique_matches}

def create_fibo_table(integer_list: list) -> list[list]:
    """Creates a table where rows consist of integers and (if they belong) fibonacci numbers."""
    headers = ["previous Fibonacci number", "observed number", "next Fibonacci number"]
    numbers = [get_prev_next_fibo(integer) for integer in integer_list]
    table = [headers]
    table.extend(numbers)
    return table