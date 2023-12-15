import hashlib

def func2(pincode):
    pincode = int.from_bytes(pincode.encode(), 'big')
    pincode = bin(abs(hash(pincode)))
    pincode = bytes(pincode, 'ascii')
    pincode = hashlib.sha1(pincode)
    pincode = pincode.hexdigest()
    pincode = bin(int.from_bytes(pincode.encode(), 'big'))[2:]
    return pincode