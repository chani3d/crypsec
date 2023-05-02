def vigenere_encode(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            # Get the numerical value of the character, where A=0, B=1, etc.
            char_num = ord(char.upper()) - 65
            # Get the numerical value of the corresponding key character
            key_char_num = ord(key[key_index % len(key)].upper()) - 65
            # Add the two values together and take the result modulo 26 to get the encoded character value
            encoded_num = (char_num + key_char_num) % 26
            # Convert the encoded value back to a character and append it to the ciphertext
            ciphertext += chr(encoded_num + 65)
            # Increment the key index
            key_index += 1
        else:
            # Non-alphabetic characters are copied as-is
            ciphertext += char
    return ciphertext


if __name__ == "__main__":
    plaintext = "hello"
    keyword = "caca"
    print(vigenere_encode(plaintext, keyword))
