def sanitize_input(text):
    # Remove non-alphabetic characters and convert to lowercase
    return ''.join(c.lower() for c in text if c.isalpha())

def generate_key(plaintext, key):
    repeats = len(plaintext) // len(key)
    extended_key = (key * repeats)[:len(plaintext)]
    return extended_key



    
def main():
    plaintext_input = input("Enter plaintext: ")
    key_input = input("Enter key: ")

    plaintext = sanitize_input(plaintext_input)
    key = sanitize_input(key_input)

    extended_key = generate_key(plaintext, key)

    print("\nSanitized Plaintext:", plaintext)
    print("Sanitized Key:      ", key)
    print("Generated Key:      ", extended_key)


if __name__ == "__main__":
    main()
