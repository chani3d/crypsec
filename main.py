# ISC protocol

def message(msg):

    header = 'ISC'.encode('utf-8')  # first 3 bytes
    length = bytes()
    msgbyte = bytes()

    if ".png" or ".jpg" in msg:
        msgtype = 'i'.encode('utf-8')
    elif 'task' in msg:
        msgtype = 's'.encode('utf-8')
    else:
        msgtype = 't'.encode('utf-8')  # 4th byte
        length = (len(msg)).to_bytes(2, byteorder='big')  # 5th & 6th byte
        msgbyte = bytes()  # N next bytes

        for element in msg:
            msgbyte += ((0).to_bytes(3, byteorder='big') + element.encode('utf-8'))

    fullmsg = header + msgtype + length + msgbyte
    return fullmsg


print(message('task')
