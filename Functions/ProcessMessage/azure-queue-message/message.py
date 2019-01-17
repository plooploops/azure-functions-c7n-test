import base64
import copy
import zlib
import logging
import json
#the 'unpack' to 'pack'
#https://github.com/cloud-custodian/cloud-custodian/blob/master/c7n/actions/notify.py

# def processMessage(encoded_azure_queue_message):
#     queue_message = json.loads(zlib.decompress(base64.b64decode(encoded_azure_queue_message.content)))

# def pack(message):
#     dumped = utils.dumps(message)
#     compressed = zlib.compress(dumped.encode('utf8'))
#     b64encoded = base64.b64encode(compressed)
#     return b64encoded.decode('ascii')

def unpack(message):
    logging.info('unpack')
    return zlib.decompress(base64.b64decode(message.encode('ascii'))).decode('utf-8')
