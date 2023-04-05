def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            new_pos = (ord(char) - 65 + shift) % 26 + 65
            result += chr(new_pos)
        elif char.islower():
            new_pos = (ord(char) - 97 + shift) % 26 + 97
            result += chr(new_pos)
        else:
            result += char
    return result


def caesar_decipher(cipher_text, shift):
    return caesar_cipher(cipher_text, -shift)
