# Analyze text from file and write results to csv and json files

from text_analysis import get_integers, get_words, create_fibo_table
from req_res_manager import responses, parse_request
from s3_com_manager import upload_file_to_s3
import json, csv
import os

def lambda_handler(req, context):
    """Handles incoming HTTP request."""
    request_status = parse_request(req)

    if request_status == "success":
        text_file = req['body']

        table = get_integers(text_file)
        table = create_fibo_table(table)
        file_name = "output.csv"
        try:
            with open('/tmp/'+file_name, 'w') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerows(table)
            if upload_file_to_s3("/tmp/"+file_name, file_name): pass
            else: raise
            os.remove('/tmp/'+file_name)
        except Exception as err:
            return responses['server_err']

        words = get_words(text_file)
        file_name = "output.json"
        try:
            with open('/tmp/'+file_name, 'w') as f:
                json.dump(words, f, indent=2)
            if upload_file_to_s3("/tmp/"+file_name, file_name): pass
            else: raise
            os.remove('/tmp/'+file_name)
        except Exception as err:
            return responses['server_err']
    
    return responses[request_status]