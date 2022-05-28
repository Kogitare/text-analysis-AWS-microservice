# Checks incoming requests and gives a list of responses

import json

def parse_request(req: dict):
    """Checks if request is a text file -> (True: True, False: str)"""
    try:
        if req['headers']['content-type'] != 'text/plain': raise
    except KeyError:
        return "request_err"
    except RuntimeError:
        return "wrong_type_err"
    return True

responses = {
    "success": {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps("File analyzed.")
    },
    "wrong_content_type": {
        'statusCode': 400,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps("Wrong content type.")
    },
    "request_err": {
        'statusCode': 400,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps("Bad request.")
    },
    "server_err": {
        'statusCode': 500,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps("Internal system error")
    }
}