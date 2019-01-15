import base64
import copy
import zlib

#the 'unpack' to 'pack'
#https://github.com/cloud-custodian/cloud-custodian/blob/master/c7n/actions/notify.py

def unpack(self, message):    
    b64encoded = message.ecode('ascii')
    compressed = base64.b64decode(b64encoded)
    decompressed = zlib.decompress(compressed)
    return decompressed
