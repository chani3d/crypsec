# import random
#
# def generate_keypair(p, q):
#     # Calculate n
#     n = p * q
#
#     # Calculate phi
#     phi = (p - 1) * (q - 1)
#
#     # Choose an integer e such that 1 < e < phi and e is coprime with phi
#     e = random.randrange(1, phi)
#     while gcd(e, phi) != 1:
#         e = random.randrange(1, phi)
#
#     # Calculate d such that d * e ≡ 1 (mod phi)
#     d = modinv(e, phi)
#
#     # Return the public key (n, e) and the private key (n, d)
#     return ((n, e), (n, d))
#
# def encrypt(pk, plaintext):
#     # Unpack the public key
#     n, e = pk
#
#     # Convert each letter in the plaintext to a number according to its position in the alphabet (caps are the same and space is equal to 0)
#     numbers = [ord(c.lower()) - 96 if c.isalpha() else 0 for c in plaintext]
#
#     # Calculate c = plaintext^e mod n for each number
#     ciphertext = [pow(num, e, n) for num in numbers]
#     return ciphertext
#
# def decrypt(pk, ciphertext):
#     # Unpack the private key
#     n, d = pk
#
#     # Calculate num = ciphertext^d mod n for each number
#     numbers = [pow(num, d, n) for num in ciphertext]
#
#     # Convert each number to its corresponding letter (caps are the same and space is equal to 0)
#     plaintext = ''.join([chr(num + 96).upper() if num > 0 else ' ' for num in numbers])
#     return plaintext
#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)
#
# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('No modular inverse')
#     else:
#         return x % m
#
# # Example usage
# p = 83
# q = 97
# public_key, private_key = generate_keypair(p, q)
#
# plaintext = "hello my name is jeff and im doing weird stuf"
# print(f"Original message: {plaintext}")
#
# ciphertext = encrypt(public_key, plaintext)
# print(f"Encrypted message: {ciphertext}")
#
# decrypted = decrypt(private_key, ciphertext)
# print(f"Decrypted message: {decrypted}")
#
# print(public_key)
# print(private_key)

import random
import math
import hashlib

def euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = euclidean_algorithm(b % a, a)
        return (g, x - (b // a) * y, y)

def modular_inverse(a, m):
    g, x, y = euclidean_algorithm(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def generate_RSA_keys(p, q):
    # Choose 2 prime numbers (p and q)
    n = p * q

    # Calculate k
    k = (p - 1) * (q - 1)

    # Choose e < k coprime with k
    e = random.randrange(1, k)
    while math.gcd(e, k) != 1:
        e = random.randrange(1, k)

    # Calculate d (1 = d * e + b * k) (b < 0)
    d = modular_inverse(e, k)

    # Return the public key (n, e) and the private key (n, d)
    return (n, e), (n, d)

def knuth_lewis_lcg(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    while True:
        x = (a*x + c) % m
        yield x

def enc_rsa(public_key, msg, seed):
    n, e = public_key

    # Convert each letter of the string to a number
    letters_to_numbers = [ord(element.lower()) - 96 if element.isalpha() else 0 for element in msg]

    # Generate the LCG
    gen = knuth_lewis_lcg(seed)

    # Encrypt each number of the message
    encrypted_msg = [pow(num ^ next(gen), e, n) for num in letters_to_numbers]
    return encrypted_msg

def dec_rsa(private_key, encrypted_msg, seed):
    n, d = private_key

    # Generate the LCG
    gen = knuth_lewis_lcg(seed)

    # Decrypt each number of the encrypted message and convert it back to a letter
    decrypted_msg = ''.join([chr(pow(num ^ next(gen), d, n) + 96).upper() if num > 0 else ' ' for num in encrypted_msg])

    return decrypted_msg

# Hash
def enc_hash(msg):
    bytedstring = msg.encode('utf-8')
    h = hashlib.sha256(bytedstring).hexdigest()
    return h

# Example usage
p = 83
q = 97
public_key, private_key = generate_RSA_keys(p, q)
msg = 'hello im trying to survive'
seed = 123456789
encrypted_msg = enc_rsa(public_key, msg, seed)
print(f'The encrypted message is: {encrypted_msg}')
decrypted_msg = dec_rsa(private_key, encrypted_msg, seed)
print(f'The decrypted message is: {decrypted_msg}')
print(f'Private key is: {private_key} and public key is: {public_key}')
