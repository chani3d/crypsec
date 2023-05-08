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

            fullmsg = header + msgtype + gth + msgbyte

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

    # Knuth & Lewis Linear Congruential Generator (fake rng)
    def knuth_lewis_lcg(self, seed):
        a = 1664525
        c = 1013904223
        m = 2 ** 32
        while True:
            seed = (a * seed + c) % m
            yield seed

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

    def enc_rsa(self, public_key, msg, seed):
        n, e = public_key

        # Convert each letter of the string to a number
        letters_to_numbers = [ord(element.lower()) - 96 if element.isalpha() else 0 for element in msg]

        # LCG
        rng = self.knuth_lewis_lcg(seed)

        # Encrypt each number of the message
        encrypted_msg = [pow(num ^ next(rng), e, n) for num in letters_to_numbers]
        return encrypted_msg

    def dec_rsa(self, private_key, encrypted_msg, seed):
        n, d = private_key

        # numbers = [pow(num, d, n) for num in encrypted_msg]
        # LCG
        rng = self.knuth_lewis_lcg(seed)

        # Convert each number of the encrypted message to a letter
        # decrypted_msg = ''.join([chr(num + 96).upper() if num > 0 else ' ' for num in numbers])
        decrypted_msg = ''.join(
            [chr(pow(num ^ next(rng), d, n) + 96).upper() if num > 0 else ' ' for num in encrypted_msg])

        return decrypted_msg

    # Hash
    def enc_hash(msg):
        bytedstring = msg.encode('utf-8')
        h = hashlib.sha256(bytedstring).hexdigest()
        return h

    # Diffie-Hellmann


    #Calculates the modular exponentiation.
    def mod_exp(base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result

    # Checks whether a given number is prime.
    def is_prime(num):
        
        
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    # Generates a prime number between the given range.
    def generate_prime(min_val, max_val):
        prime = None
        while prime is None:
            num = random.randint(min_val, max_val)
            if is_prime(num):
                prime = num
        return prime

    # Generates the private and public keys for the key exchange.
    def generate_keys(self):
        self.a = random.randint(1, self.p - 1)
        self.A = mod_exp(self.g, self.a, self.p)
        return self.A

    # Generates the shared secret key using the public key of the other party.
    def generate_shared_secret(self, B):
        self.shared_secret = mod_exp(B, self.a, self.p)
        return self.shared_secret


    image_try = enc_msg('pic.png')
