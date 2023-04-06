from caesar import caesar_cipher, caesar_decipher


def test_cipher():
    plain_text = "abcDEFGHIJKLMNOPQRSTUVWXYZ123"
    cipher_text = caesar_cipher(plain_text, 1)
    assert cipher_text == "bcdEFGHIJKLMNOPQRSTUVWXYZA123"


def test_decipher():
    cipher_text = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
    plain_text = caesar_decipher(cipher_text, 1)
    assert plain_text == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
