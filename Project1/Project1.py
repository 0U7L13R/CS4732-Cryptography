def sanitize_input(text):                                     # Remove non-alphabetic characters and convert to lowercase
    return ''.join(c.lower() for c in text if c.isalpha())

def vigenere_encrypt():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    # Sanitize inputs
    plaintext = sanitize_input(plaintext)
    key = sanitize_input(key)
