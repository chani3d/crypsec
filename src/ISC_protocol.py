from PIL import Image


class IscProtocol:

    # Message
    def enc_msg(msg):

        header = 'ISC'.encode('utf-8')  # first 3 bytes

        if '.png' in msg:
            msgtype = 'i'.encode('utf-8')
            img = Image.open(msg).convert('RGB')
            width, height = img.size
            bytergb = bytes()

            for x in range(img.height):
                for y in range(img.width):
                    r, g, b = img.getpixel((y, x))
                    byter = r.to_bytes(1, 'big')
                    byteg = g.to_bytes(1, 'big')
                    byteb = b.to_bytes(1, 'big')
                    bytergb += byter + byteg + byteb

            fullmsg = header + msgtype + width.to_bytes(1, 'big') + height.to_bytes(1, 'big') + bytergb

        else:
            if 'task' in msg:
                msgtype = 's'.encode('utf-8')  # 4th byte of a command
            else:
                msgtype = 't'.encode('utf-8')  # 4th byte of a text

            length = (len(msg)).to_bytes(2, 'big')  # 5th & 6th byte
            msgbyte = bytes()  # N next bytes

            for element in msg:
                # msgbyte += ((0).to_bytes(4, 'big')) + element.encode('utf-8')
                msgbyte += (ord(element)).to_bytes(4, 'big')

            fullmsg = header + msgtype + length + msgbyte

        return fullmsg

    def dec_msg(msg:bytes):

        btostr = msg.decode('utf-8')
        cleanstr = btostr.replace('ISCt', '')

        return cleanstr

    # Vigenere
    def enc_vgnr(msg):
        pass

    def dec_vgnr(msg):
        pass

    # RSA
    def enc_rsa(msg):
        pass

    def dec_rsa(msg):
        pass

    #print(enc_msg('Test'))
