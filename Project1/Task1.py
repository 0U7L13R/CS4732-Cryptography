def sanitize_input(text):
    return ''.join(c.lower() for c in text if c.isalpha()) # changes to lowercase IF the char is alphabetical


def generate_key(plaintext, key):
    repeats = len(plaintext) // len(key) + 1
    extended_key = (key * repeats)[:len(plaintext)]  # I exaggerated the key since I slice off anything extra at the end. +1 so it's never *1
    return extended_key


def vigenere_encrypt_list(plaintext, key):
    encrypted_chars = [] 
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('a')  # Convert 'a' to 'z' to 0–25
        k = ord(key[i]) - ord('a')
        c = (p + k) % 26  # Modular arithmetic if it exceeds 'z'
        encrypted_char = chr(c + ord('a'))  # Convert back to char
        encrypted_chars.append(encrypted_char)
    return ''.join(encrypted_chars)


def vigenere_decrypt_list(ciphertext, key):
    decrypted_chars = []
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('a')
        k = ord(key[i]) - ord('a')
        p = (c - k + 26) % 26  # +26 makes sure to stay positive before mod, it's adding a whole essentially
        decrypted_char = chr(p + ord('a'))
        decrypted_chars.append(decrypted_char)
    return ''.join(decrypted_chars)


def main():
    plaintext_input = input("Enter plaintext: ")
    key_input = input("Enter key: ")

    # sanatize
    plaintext = sanitize_input(plaintext_input)
    key = sanitize_input(key_input)

    # Validate input
    if len(plaintext) == 0 or len(key) == 0:
        print("Error: Plaintext and key must contain an alphabetic char")
        return

    #Makes the key exactly as long as the plaintext after sanitization
    extended_key = generate_key(plaintext, key)

    #Encrypt and decrypt
    ciphertext = vigenere_encrypt_list(plaintext, extended_key)
    decrypted_text = vigenere_decrypt_list(ciphertext, extended_key)

    #output
    print("\nSanitized Plaintext: ", plaintext)
    print("Generated Key:        ", extended_key)
    print("Ciphertext:           ", ciphertext)
    print("Decrypted Plaintext:  ", decrypted_text)


if __name__ == "__main__":
    main()
