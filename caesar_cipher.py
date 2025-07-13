
def caesar_encrypt(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("\n🔵 Prodigy - Caesar Cipher 🔐")
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == '1':
        text = input("\nEnter the message to encrypt: ")
        shift = int(input("Enter shift value (e.g., 3): "))
        encrypted = caesar_encrypt(text, shift)
        print(f"\n🔒 Encrypted Message: {encrypted}\n")

    elif choice == '2':
        text = input("\nEnter the message to decrypt: ")
        shift = int(input("Enter shift value used during encryption: "))
        decrypted = caesar_decrypt(text, shift)
        print(f"\n🔓 Decrypted Message: {decrypted}\n")

    elif choice == '3':
        print("\nGoodbye! 👋")
        exit()

    else:
        print("\nInvalid choice. Please try again.\n")

if __name__ == '__main__':
    while True:
        main()
        input("Press Enter to continue...")
