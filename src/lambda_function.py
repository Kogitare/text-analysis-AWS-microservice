# Analyze text from file and write results to csv and json files

from text_analysis import get_integers, get_words, create_fibo_table
import json
import csv

def lambda_handler(event, context):
    text = event['body']
    fib_numbers = create_fibo_table(get_integers(text))
    words = get_words(text)
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            "words": words,
            "numbers": fib_numbers
        })
    }