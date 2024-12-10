import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = []
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text.append(letter)
            continue
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    output_text = ''.join(output_text)
    print(f"Here is the {encode_or_decode}d result: {output_text}")

caesar_game = False

while caesar_game is False:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Do you want to restart the encode/decode program? Type 'Yes', or 'No'.\n").lower()
    if restart == "yes":
        caesar_game = False
    elif restart == "no":
        caesar_game = True
    else:
        print("You have entered an invalid option")



