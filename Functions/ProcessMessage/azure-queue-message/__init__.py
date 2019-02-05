import logging
import azure.functions as func
import json
import zlib
import base64
from . import message

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        #local debugging with the raw input
        #logging.info(req.get_json())
        #json_contents = req.get_json()
        #body = json_contents.get('body')
        body = req.get_body()
        logging.info(body)
        results = message.unpack(body)
        return func.HttpResponse(body=results, headers={ "Content-Type" : "application/json" })
    except Exception as e:
        logging.info(e)
        pass
