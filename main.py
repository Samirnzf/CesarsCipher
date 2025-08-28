
def caesar_cipher(message, shift, mode="encode"):
    output = ""
    for letter in message:
        ascii_value = ord(letter)

        if 'a' <= letter <= 'z':  # only shift lowercase letters
            if mode == "encode":
                ascii_value = (ascii_value - 97 + shift) % 26 + 97
            elif mode == "decode":
                ascii_value = (ascii_value - 97 - shift) % 26 + 97

        output += chr(ascii_value)

    print("\n" + "=" * 40)
    print(f"🔐 Here's the {mode}d result: {output}")
    print("=" * 40 + "\n")


def main():
    print("=" * 40)
    print("   ✨ Welcome to the Caesar Cipher ✨")
    print("=" * 40)

    while True:
        choice = input("\n👉 Type 'encode' to encrypt, 'decode' to decrypt: ").lower()

        if choice not in ["encode", "decode"]:
            print("⚠️  Please enter a valid option (encode/decode).")
            continue

        user_message = input("💬 Enter your message: ").lower()
        shift_number = int(input("🔢 Enter the shift number: "))

        caesar_cipher(user_message, shift_number, choice)

        answer = input("🔄 Do you want to try again? (y/n): ").lower()
        if answer != "y":
            print("\n👋 Thanks for using the Caesar Cipher. Goodbye!")
            break


if __name__ == "__main__":
    main()