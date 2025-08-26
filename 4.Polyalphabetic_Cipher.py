def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    j = 0  

    for char in plaintext:
        if char.isalpha():
            p = ord(char) - ord('A')
            k = ord(key[j % len(key)]) - ord('A')
            c = (p + k) % 26
            ciphertext += chr(c + ord('A'))
            j += 1
        else:
            ciphertext += char 
    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    j = 0

    for char in ciphertext:
        if char.isalpha():
            c = ord(char) - ord('A')
            k = ord(key[j % len(key)]) - ord('A')
            p = (c - k + 26) % 26
            plaintext += chr(p + ord('A'))
            j += 1
        else:
            plaintext += char
    return plaintext

message = "AKARSH JHA"
key = "KEY"

encryption = encrypt(message, key)
print("Encryption:", encrypted)

decryption = decrypt(encrypted, key)
print("Decryption:", decrypted)
