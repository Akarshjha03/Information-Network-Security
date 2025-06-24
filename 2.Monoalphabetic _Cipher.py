import string

# Custom fixed key: shuffled letters + digits + space
CUSTOM_KEY = 'qazwsxedcrfvtgbyhnujmikolp0987654321 '

def create_translation_table(source, target):
    return str.maketrans(source, target)

def encrypt(plaintext, key):
    # Full alphabet includes lowercase + digits + space
    original_alphabet = string.ascii_lowercase + string.digits + ' '
    translation_table = create_translation_table(original_alphabet, key)
    return plaintext.lower().translate(translation_table)

def decrypt(ciphertext, key):
    original_alphabet = string.ascii_lowercase + string.digits + ' '
    translation_table = create_translation_table(key, original_alphabet)
    return ciphertext.translate(translation_table)

# Example usage
if __name__ == "__main__":
    key = CUSTOM_KEY
    print(f"Key used: {key}")

    plaintext = "secure 123 transmission"
    print(f"Plaintext: {plaintext}")

    ciphertext = encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")

    decrypted = decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted}")
