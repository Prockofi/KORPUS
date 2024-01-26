import hashlib
from secret import Secret

def func2(pincode):
    cript = Secret()
    pincode = cript.hash(pincode)
    return pincode