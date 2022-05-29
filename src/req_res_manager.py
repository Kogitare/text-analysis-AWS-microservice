# Checks incoming requests and gives a list of responses

import json

def parse_request(req: dict) -> str:
    """Checks if request checks requirements"""
    size_limit = 1000000    # 1MB
    if "body" not in req.keys() or "headers" not in req.keys():
        return "request_err"
    if "content-type" not in req['headers'].keys() or "content-length" not in req['headers'].keys():
        return "request_err"
    if req['headers']['content-type'] != 'text/plain':
        return "wrong_content_type"
    if int(req['headers']['content-length']) > size_limit or len(req['body']) > size_limit:
        return "too_large"
    return "success"

responses = {
    "success": {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            "message": "File Analyzed"
        })
    },
    "wrong_content_type": {
        'statusCode': 415,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            "message": "Wrong Content Type"
        })
    },
    "request_err": {
        'statusCode': 400,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            "message": "Bad Request"
        })
    },
    "too_large": {
        'statusCode': 413,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            "message": "Payload Too Large"
        })
    },
    "server_err": {
        'statusCode': 500,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            "message": "Internal System Error"
        })
    }
}