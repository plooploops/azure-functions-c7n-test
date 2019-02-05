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
        # dumped = utils.dumps(message)
        # compressed = zlib.compress(dumped.encode('utf8'))
        # b64encoded = base64.b64encode(compressed)
        # if not encode_ascii: 
        #     return str(b64encoded)
        # else:
        #     return b64encoded.decode('ascii')

def unpack(message):
    logging.info(message)

    # skip the first two characters and last character for "b'MESSAGECONTENTS'"
    if len(message) > 2 and message[:2:] == "b'" and message[-1] == "'":
        return zlib.decompress(base64.b64decode(message[2:-1:])).decode('utf-8')
    # skip the first two characters and last character for b"b'contents'"
    elif len(message) > 2 and message[:2] == b"b'":
        return zlib.decompress(base64.b64decode(message[2:-1:])).decode('utf-8')    
    return zlib.decompress(base64.b64decode(message)).decode('utf-8')    
