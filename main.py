# Analyze text from file and write results to csv and json files

from text_analysis import get_integers, get_words, create_fibo_table
import json
import csv

def parse_file(path) -> tuple[list[list], dict]:
    """Analyze integers and words in specific file."""
    with open(path, 'r') as f:
        contents = f.read()
        fib_numbers = create_fibo_table(get_integers(contents))
        words = get_words(contents)
        return fib_numbers, words

def save_list_as_csv(table_header: list, table_data: list, path: str, filename = 'output.csv'):
    """Save table into a csv file."""
    with open(path+filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(table_header)
        writer.writerows(table_data)

def save_dict_as_json(dictionary: dict, path: str, filename = 'output.json'):
    """Save dictionary into json file"""
    with open(path+filename, 'w') as f:
        json.dump(dictionary, f)

# Run script locally
if __name__ == "__main__":
    path_in = './input/text_in.txt'
    path_out = './output/'
    csv_header = ['previous Fibonacci number', 'observed number', 'next Fibonacci number']
    parsed = parse_file(path_in)
    save_list_as_csv(csv_header, parsed[0], path_out)
    save_dict_as_json(parsed[1], path_out)