# Analyze text from file and write results to csv and json files

import text_analysis
import json
import csv

def parse_file(path):
    with open(path, 'r') as f:
        contents = f.read()
        fib_numbers = text_analysis.get_fibonacci(text_analysis.get_integers(contents))
        words = text_analysis.get_words(contents)
        return fib_numbers, words

def save_list_as_csv(table_headers: list, table_data: list, path: str, filename = 'numbers.csv'):
    with open(path+filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(table_headers)
        writer.writerows(table_data)

def save_dict_as_json(dictionary: dict, path: str, filename = 'words.json'):
    with open(path+filename, 'w') as f:
        json.dump(dictionary, f)

if __name__ == "__main__":
    path_in = './input/text_in.txt'
    path_out = './output/'
    csv_headers = ['previos Fibonacci number', 'observed number', 'next Fibonacci number']
    parsed = parse_file(path_in)
    save_list_as_csv(csv_headers, parsed[0], path_out)
    save_dict_as_json(parsed[1], path_out)