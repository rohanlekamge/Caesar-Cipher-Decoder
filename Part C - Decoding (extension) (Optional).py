#Part C: Decoding (Extension)

print("1. 'e' for Encoding")
print("2. 'd' for Decoding")
print("3. 'q' to Quit")

command = input("\nEnter Your Command: ")
while command != "q":
    if command == "e":
        plaintext = input("Enter Your Message Here: ")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key = int(input("Enter Your Shifting Value Between 1 and 25: "))
        cipher = ""

        for c in plaintext:
            if c in alphabet:
                cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
            else:
                cipher += c
        print("Your Encrypted Message is: ", cipher)
        print()
        print("--------------------------------------")


    elif command == "d":
        plaintext = input("Enter Your Message Here: ")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        hint = input("Enter First Word Here: ")
        first = plaintext[0]
        second = hint[0]
        key1 = plaintext.index(first) - alphabet.index(first)
        key2 = hint.index(second) - alphabet.index(second)
        key = key2 - key1
        cipher = ""     #I have used arrays in this program

        for c in plaintext:
            if c in alphabet:
                cipher += alphabet[(alphabet.index(c)-key)%(len(alphabet))]
            else:
                cipher += c

        print("Your Encrypted Message is: ", cipher)
        print("Shifting Value is",key)
        print()
        print("--------------------------------------")

    command = input("\nEnter Your Command: ")










