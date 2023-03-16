from PIL import Image


class IscProtocol:

    def message(msg):

        header = 'ISC'.encode('utf-8')  # first 3 bytes
        length = bytes()
        msgbyte = bytes()
        msgtype = ''

        if '.png' in msg:
            msgtype = 'i'.encode('utf-8')
            img = Image.open(msg).convert('RGB')
            width, height = img.size
            bytergb = bytes()

            for x in range(img.height):
                for y in range(img.width):
                    r, g, b = img.getpixel((y, x))
                    byter = r.to_bytes(1, byteorder='big')
                    byteg = g.to_bytes(1, byteorder='big')
                    byteb = b.to_bytes(1, byteorder='big')
                    bytergb += byter + byteg + byteb

            fullmsg = header + msgtype + width.to_bytes(1, byteorder='big') + height.to_bytes(1,
                                                                                              byteorder='big') + bytergb

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
