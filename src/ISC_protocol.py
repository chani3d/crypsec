from PIL import Image
import random
import math
import hashlib


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

    def dec_msg(msg):
        btostr = msg.decode('utf-8')

        if btostr.startswith('ISCt'):
            cleanstr = btostr.replace('ISCt', '')

        elif btostr.startswith('ISCi'):
            pass
            cleanstr = btostr.replace('ISCi', '')
            cleanstr = bt

        elif btostr.startswith('ISCs'):
            cleanstr = btostr.replace('ISCs', '')


        return cleanstr


    # Shift
    def shift(msg, key):
        cryptedstring = ''

        for element in msg:
            cryptedstring += chr(ord(element) + key)
            
        return cryptedstring


    # Vigenere
    def enc_vgnr(plaintext, key):
        cipher_text = []
        for i in range(len(plaintext)):
            x = (ord(plaintext[i]) +
                 ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return("" . join(cipher_text))

    def dec_vgnr(ciphertext, key):
        # Repeat the keyword to match the length of the ciphertext
        keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

        # Generate the plaintext by shifting each character of the ciphertext backwards by the
        # corresponding character of the keyword using the Vigenère table
        plaintext = ''
        for i in range(len(ciphertext)):
            ciphertext_char = ciphertext[i]
            keyword_char = keyword[i]
            shift = ord(keyword_char) - ord('A')
            plaintext_char = chr((ord(ciphertext_char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += plaintext_char

        return plaintext

    # RSA
    def generate_keys():
        # Choose two large distinct prime numbers
        p = 31
        q = 37

        # Calculate n and phi(n)
        n = p * q
        phi_n = (p - 1) * (q - 1)

        # Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
        e = random.randint(2, phi_n - 1)
        while math.gcd(e, phi_n) != 1:
            e = random.randint(2, phi_n - 1)

        # Calculate the modular multiplicative inverse d of e modulo phi(n)
        d = pow(e, -1, phi_n)

        # Return the public and private keys as tuples of two values each: (n, e) and (n, d)
        public_key = (n, e)
        private_key = (n, d)

        return (public_key, private_key)

    def dec_rsa(msg, key):
        n, k = key
        return pow(message, k, n)
    # Hash
    def enc_hash(msg):
        bytedstring = msg.encode('utf-8')
        h = hashlib.sha256(bytedstring).hexdigest()
        return h
        
    plaintext = 'hello world'
    key = 'key'    
    # Test
    print(enc_vgnr(plaintext, key))
