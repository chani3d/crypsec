# import random
# import math
#
# def euclidean_algorithm(a, b):
#     if a == 0:
#         return(b, 0, 1)
#     else:
#         g, y, x = euclidean_algorithm(b % a, a)
#         return (g, x - (b // a) * y, y)
#
# def modular_inverse(a, m):
#     g, x, y = euclidean_algorithm(a, m)
#     if g != 1:
#         raise Exception('Modular inverse does not exist')
#     else:
#         return x % m
#
#
#
# #     # Choose 2 prime numbers (p qnd q)
# # def generate_public_key(p, q):
# #     # Calculate n = pq
# #     n = p * q
# #
# #     # Calculate k
# #     k = (p - 1) * (q - 1)
# #
# #     # Choose e < k coprime with k
# #     e = random.randrange(1, k)
# #     while math.gcd(e, k) != 1:
# #         e = random.randrange(1, k)
# #         
# #     # Return public (n, e) key
# #     return (n, e)
# #
# # def generate_private_key(p, q):
# #     # Calculate n = pq
# #     n = p * q
# #
# #     # Calculate k
# #     k = (p - 1) * (q - 1)
# #
# #     # Choose e < k coprime with k
# #     e = random.randrange(1, k)
# #     while math.gcd(e, k) != 1:
# #         e = random.randrange(1, k)
# #
# #     # Calculate d (1 = d * e + b * k) (b < 0)
# #     d = modular_inverse(e, k)
# #
# #     # Return private (n, d) key
# #     return (n, d)
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
#     while math.gcd(e, phi) != 1:
#         e = random.randrange(1, phi)
#
#     # Calculate d such that d * e ≡ 1 (mod phi)
#     d = modular_inverse(e, phi)
#
#     # Return the public key (n, e) and the private key (n, d)
#     return ((n, e), (n, d))
#
# ydef enc_rsa(public_key, msg):
#     n, e = public_key
#
#     # Convert each letter of the string to a number
#     letters_to_numbers = [ord(element.lower()) - 96 if element.isalpha() else 0 for element in msg]
#
#     encrypted_msg = [pow(num, e, n) for num in letters_to_numbers]
#     return encrypted_msg
#
# def dec_rsa(private_key, encrypted_msg):
#     n, d = private_key
#
#     numbers = [pow(num, d, n) for num in encrypted_msg]
#
#     # Convert each number of the encrypted message to a letter
#     decrypted_msg = ''.join([chr(num + 96).upper() if num > 0 else ' ' for num in numbers])
#
#     return decrypted_msg
#
#
# p = 83
# q = 97
#
# # public_key = generate_public_key(p, q)
# # private_key = generate_private_key(p, q)
#
# public_key, private_key = generate_keypair(p, q)
#
# msg = 'hello im trying to survive'
# encrypted_msg = enc_rsa(public_key, msg)
# print(f'The encrypted message is: {encrypted_msg}')
# decrypted_msg = dec_rsa(private_key, encrypted_msg)
# print(f'The decrypted message is: {decrypted_msg}')
#
# print(f'private key is: {private_key} and public key is: {public_key}')
#
#
