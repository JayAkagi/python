import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

app_running = True

print(art.logo)
while app_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift):
        secret_message = ""
        for char in text:
            if char in alphabet:
                index = alphabet.index(char)
                if direction == "encode":
                    new_char = (index + shift) % 26
                elif direction == "decode":
                    new_char = (index - shift) % 26
                secret_message += alphabet[new_char]
            else:
                secret_message += char
        print(f"The {direction}d text is: {secret_message}")

    caesar(text, shift)

    final_prompt = True
    while final_prompt:
        exit = input("Type \"Yes\" if you want to go again. Otherwise, type \"No\".").lower()
        if exit == "yes":
            app_running = True
            final_prompt = False
        elif exit == "no":
            app_running = False
            final_prompt = False
            print("Goodbye!")
        else:
            print("Invalid option. try again.\n")




