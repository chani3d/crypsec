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


