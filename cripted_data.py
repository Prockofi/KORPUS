from secret import Secret

def cripted(password, name, pincode):
    data = name + '%/%/%' + password
    cript = Secret()
    cript.key(pincode)
    data = cript.cripto(data)
    return data

def decripted(res, pincode):
    cript = Secret()
    cript.key(pincode)
    data = cript.cripto(res)
    try:
        name, password = data.split('%/%/%')
    except:
        name, password = ['Пароль не подошёл', '']
    return password, name