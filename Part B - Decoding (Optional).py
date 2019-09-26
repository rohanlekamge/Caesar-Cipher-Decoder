#Part B: Decoding 

print("1. 'e' for Encoding")
print("2. 'd' for Decoding")
print("3. 'q' to Quit")

command = input("\nEnter Your Command: ")
while command != "q":
    if command == "e":
        plaintext = input("Enter Your Message Here: ")      #user should enter a message to encrypt in here
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key = int(input("Enter Your Shifting Value Between 1 and 25: "))    #user should enter the shifting value in here
        cipher = ""

        for c in plaintext:
            if c in alphabet:
                cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
            else:                                           #cipher is just a variable
                cipher += c                                 #I have used MOD in this program to find the shifting value
        print("Your Encrypted Message is: ", cipher)
        print()
        print("--------------------------------------")


    elif command == "d":
        plaintext = input("Enter Your Message Here: ")
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key = int(input("Enter Your Shifting Value Between 1 and 25: "))
        cipher = ""

        for c in plaintext:
            if c in alphabet:
                cipher += alphabet[(alphabet.index(c)-key)%(len(alphabet))]
            else:
                cipher += c

        print("Your Encrypted Message is: ", cipher)
        print()
        print("--------------------------------------")

    command = input("\nEnter Your Command: ")








