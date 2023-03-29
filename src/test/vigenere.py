

#Shift (implemented in ISC_protocol)

def shifenc(originalstring, key):
    cryptedstring = ''

    for element in originalstring:
        cryptedstring += chr(ord(element) + key)
    
    return cryptedstring


