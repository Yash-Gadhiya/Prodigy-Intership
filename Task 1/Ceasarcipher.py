def encrypt(text, shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Keep other characters unchanged
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Get inputs from the user
text = input("Enter the text: ")
shift = int(input("Enter the shift number: "))
choice = input("Do you want to encrypt or decrypt? (e/d): ")

if choice.lower() == 'e':
    print("Encrypted text: " + encrypt(text, shift))
elif choice.lower() == 'd':
    print("Decrypted text: " + decrypt(text, shift))
else:
    print("Invalid choice")
