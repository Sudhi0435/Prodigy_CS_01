def caesar_cipher(message, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in message:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    
    while True:
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))
        mode = input("Choose mode (encrypt/decrypt): ").lower()

        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
            continue

        encrypted_message = caesar_cipher(message, shift, mode)
        print("Result:", encrypted_message)
        
        cont = input("Do you want to continue? (yes/no): ").lower()
        if cont != 'yes':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()
