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
    def enc_vgnr(msg, key):
        ciphered_msg = ""
        key_index = 0
        for char in msg:
            if char.isalpha():
                # Get the numerical value of the character, where A=0, B=1, etc.
                char_num = ord(char.upper()) - 65
                # Get the numerical value of the corresponding key character
                key_char_num = ord(key[key_index % len(key)].upper()) - 65
                # Add the two values together and take the result modulo 26 to get the encoded character value
                encoded_num = (char_num + key_char_num) % 26
                # Convert the encoded value back to a character and append it to the ciphertext
                ciphered_msg += chr(encoded_num + 65)
                # Increment the key index
                key_index += 1
            else:
                # Non-alphabetic characters are copied as they are
                ciphered_msg += char
        return ciphered_msg

    def dec_vgnr(ciphertext, keyword):
        plaintext = ""
        keyword_index = 0
        for c in ciphertext:
            if c.isalpha():
                # Determine the shift value for the current character
                shift = ord(keyword[keyword_index % len(keyword)]) - ord('a')
                # Decrypt the current character using the shift value
                if c.isupper():
                    plaintext += chr((ord(c) - shift - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(c) - shift - 97) % 26 + 97)
                # Move to the next letter in the keyword
                keyword_index += 1
            else:
                # Keep non-alphabetic characters as-is
                plaintext += c
        return plaintext

    # RSA

    def __init__(self, p=None, q=None):
        if p is not None and q is not None:
            self.public_key, self.private_key = self.generate_RSA_keys(p, q)

    def euclidean_algorithm(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.euclidean_algorithm(b % a, a)
            return (g, x - (b // a) * y, y)

    def modular_inverse(self, a, m):
        g, x, y = self.euclidean_algorithm(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    """
    An important thing for RSA !!! : do not generate private and public keys separately (two different methods), 
    otherwise we won't be able to decryp well as p and q from first method can change in the second one !!!
    """

    def generate_RSA_keys(self, p, q):
        # Choose 2 prime numbers (p and q)
        n = p * q

        # Calculate k
        k = (p - 1) * (q - 1)

        # Choose e < k coprime with k
        e = random.randrange(1, k)
        while math.gcd(e, k) != 1:
            e = random.randrange(1, k)

        # Calculate d (1 = d * e + b * k) (b < 0)
        d = self.modular_inverse(e, k)

        # Return the public key (n, e) and the private key (n, d)
        return (n, e), (n, d)

    def enc_rsa(self, public_key, msg):
        n, e = public_key

        # Convert each letter of the string to a number
        letters_to_numbers = [ord(element.lower()) - 96 if element.isalpha() else 0 for element in msg]

        encrypted_msg = [pow(num, e, n) for num in letters_to_numbers]
        return encrypted_msg

    def dec_rsa(self, private_key, encrypted_msg):
        n, d = private_key

        numbers = [pow(num, d, n) for num in encrypted_msg]

        # Convert each number of the encrypted message to a letter
        decrypted_msg = ''.join([chr(num + 96).upper() if num > 0 else ' ' for num in numbers])

        return decrypted_msg

    # Hash
    def enc_hash(msg):
        bytedstring = msg.encode('utf-8')
        h = hashlib.sha256(bytedstring).hexdigest()
        return h


tryy = IscProtocol()
p = 83
q = 97
public_key, private_key = tryy.generate_RSA_keys(p, q)
msg = 'hello im trying to survive'
encrypted_msg = tryy.enc_rsa(public_key, msg)
print(f'The encrypted message is: {encrypted_msg}')
decrypted_msg = tryy.dec_rsa(private_key, encrypted_msg)
print(f'The decrypted message is: {decrypted_msg}')

print(f'private key is: {private_key} and public key is: {public_key}')
