import itertools

def sanitize_input(text):
    return ''.join(c.lower() for c in text if c.isalpha()) # changes to lowercase IF the char is alphabetical

def generate_key(text, key):
    repeats = len(text) // len(key) + 1  # I exaggerated the key since I slice off anything extra at the end. +1 so it's never *1
    return (key * repeats)[:len(text)]

def vigenere_decrypt(ciphertext, key):
    decrypted_chars = []
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('a')  # Convert 'a' to 'z' to 0–25
        k = ord(key[i]) - ord('a')
        p = (c - k + 26) % 26  # Modular arithmetic if it exceeds 'z'
        decrypted_chars.append(chr(p + ord('a')))  # Convert back to char
    return ''.join(decrypted_chars)

def brute_force_vigenere(ciphertext, known_substring, max_key_length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key_length in range(1, max_key_length + 1):
        print(f"\nAttempting key length {key_length}")

        # Generate all combinations of a-z for the current key length
        for key_tuple in itertools.product(alphabet, repeat=key_length):
            key = ''.join(key_tuple)  # Turn tuple ('a','b','c') into "abc"
            extended_key = generate_key(ciphertext, key)  # make key to match ciphertext
            decrypted_text = vigenere_decrypt(ciphertext, extended_key)

            # substring match
            if known_substring in decrypted_text:
                print(f"\nPossible Match Discovered")
                print(f"Key: {key}")
                print(f"Plaintext: {decrypted_text}")

                # Prompt to keep attempt after finding a match
                response = input("Continue attempt? (y/n) ").strip().lower()
                if response != 'y':
                    print("Stopped")
                    return  # exit if user says n

        # After trying all keys of a length, ask user to continue
        response = input(f"Finished key length {key_length}. Continue to length {key_length + 1}? (y/n): ").strip().lower()
        if response != 'y':
            print("Stopped")
            return

    print("No valid key was discovered.")



def main():
    print("(sorta) Brute Force Vigenère")

    ciphertext_input = input("Enter ciphertext: ")
    known_substring_input = input("Enter known substring in plaintext: ")
    max_key_length_input = input("Enter max key length to attempt (1–10): ")

    # Sanitize both ciphertext and substring
    ciphertext = sanitize_input(ciphertext_input)
    known_substring = sanitize_input(known_substring_input)

    # Input validation for key length
    try:
        max_key_length = int(max_key_length_input)
        if not 1 <= max_key_length <= 10:
            raise ValueError
    except ValueError:
        print("Error: Enter a number between 1 and 10")
        return

    # Begin attempt
    brute_force_vigenere(ciphertext, known_substring, max_key_length)

# Entry point
if __name__ == "__main__":
    main()
