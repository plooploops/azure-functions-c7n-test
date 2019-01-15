import logging
import azure.functions as func
from . import message

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_json()
        message_text = req_body.get('messagetext')
        results = message.unpack(message_text)
        return func.HttpResponse(results)
    except ValueError:
        pass