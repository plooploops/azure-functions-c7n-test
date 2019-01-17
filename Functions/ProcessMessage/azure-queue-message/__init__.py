import logging
import azure.functions as func
import json
import zlib
import base64
from . import message

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        logging.info(req.get_json())
        json_contents = req.get_json()
        body = json_contents.get('body')
        results = message.unpack(body)
        return func.HttpResponse(results)
        # return func.HttpResponse(json.dumps(results))
    except Exception:
        pass
