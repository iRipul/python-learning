from artwork import logo

#Welcome Screen
print(logo)

#Initialization
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# function area
def caesar(text,shift,direction):
    if direction == "decode":
        shift *= -1
    result_text = ""
    for char in text:
        if char in alphabet:
            postition = alphabet.index(char)
            new_position = postition + shift
            result_text += alphabet[new_position]
        else:
            result_text += char
            
    print(f"The {direction}d text is {result_text}")


#Input
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text,shift,direction)

    ans = input("Do you wanna continue? yes or no\n").lower()
    if ans == "no":
        should_continue = False
        print("Good Bye!!")
