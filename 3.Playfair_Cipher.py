def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    key = "".join(sorted(set(key), key=key.index))  # Remove duplicates, preserve order
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is omitted

    for char in alphabet:
        if char not in key:
            key += char

    matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
    return matrix


def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))

    i = 0
    prepared = ""
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'X'

    return prepared


def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(a, matrix)
    row2, col2 = find_position(b, matrix)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    prepared_text = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(prepared_text), 2):
        a = prepared_text[i]
        b = prepared_text[i+1]
        ciphertext += encrypt_pair(a, b, matrix)

    return ciphertext


def decrypt_pair(a, b, matrix):
    row1, col1 = find_position(a, matrix)
    row2, col2 = find_position(b, matrix)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i+1]
        plaintext += decrypt_pair(a, b, matrix)

    return plaintext


def clean_plaintext(text):
    cleaned = ""
    i = 0
    while i < len(text):
        if i < len(text)-2 and text[i] == text[i+2] and text[i+1] == 'X':
            cleaned += text[i]
            i += 2
        else:
            cleaned += text[i]
            i += 1
    if cleaned.endswith('X'):
        cleaned = cleaned[:-1]
    return cleaned


# Example usage:
key = "HELIX"
plaintext = "AKARSH"
ciphertext = playfair_encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted = playfair_decrypt(ciphertext, key)
print("Decrypted (raw):", decrypted)
print("Cleaned Decryption:", clean_plaintext(decrypted))
