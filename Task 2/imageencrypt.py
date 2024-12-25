from PIL import Image
import random

def encrypt_image(input_path, output_path, key):
    """
    Encrypts an image by manipulating its pixel values.

    Args:
        input_path (str): Path to the input image.
        output_path (str): Path to save the encrypted image.
        key (int): Encryption key (used to modify pixel values).
    """
    # Open the image
    image = Image.open(input_path)
    pixels = image.load()

    # Get image dimensions
    width, height = image.size

    # Encrypt the pixels
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Modify pixel values using the key
            r_encrypted = (r + key) % 256
            g_encrypted = (g + key) % 256
            b_encrypted = (b + key) % 256

            # Set the new pixel value
            pixels[x, y] = (r_encrypted, g_encrypted, b_encrypted)

    # Save the encrypted image
    image.save(output_path)
    print(f"Image encrypted and saved at {output_path}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypts an image by reversing pixel manipulation.

    Args:
        input_path (str): Path to the encrypted image.
        output_path (str): Path to save the decrypted image.
        key (int): Encryption key (used to reverse pixel modification).
    """
    # Open the image
    image = Image.open(input_path)
    pixels = image.load()

    # Get image dimensions
    width, height = image.size

    # Decrypt the pixels
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Reverse the modification using the key
            r_decrypted = (r - key) % 256
            g_decrypted = (g - key) % 256
            b_decrypted = (b - key) % 256

            # Set the new pixel value
            pixels[x, y] = (r_decrypted, g_decrypted, b_decrypted)

    # Save the decrypted image
    image.save(output_path)
    print(f"Image decrypted and saved at {output_path}")

# Example usage
if __name__ == "__main__":
    input_image = r"D:\intership\Task 2/Yash.jpeg"  # Replace with the path to your image
    encrypted_image = r"D:\intership\Task 2\Output/encrypted_image.jpg"
    decrypted_image = r"D:\intership\Task 2\Outputdecrypted_image.jpg"

    key = int(input("Enter an encryption key (1-255): "))  
    print(f"Encryption Key: {key}")

    # Encrypt the image
    encrypt_image(input_image, encrypted_image, key)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image, key)
