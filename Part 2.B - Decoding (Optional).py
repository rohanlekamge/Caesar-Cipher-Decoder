#Part B: Decoding 

print("1. 'e' for Encoding")
print("2. 'd' for Decoding")
print("3. 'q' to Quit")

command = input("\nEnter Your Command: ")   #taking the input to run the program.
while command != "q":         #this is loop which runs until command = q.
    if command == "e":        #if this happens following processes will happen.
        plaintext = input("Enter Your Message Here: ")      #user should enter a message to encrypt in here.
        alphabet = "abcdefghijklmnopqrstuvwxyz"             #created list 'alphabet' and append letters in the English Alphabet.  
        key = -1
        while key < 1 or key > 25:
            key = int(input("Enter Your Shifting Value Between 1 and 25: "))    #user should enter the shifting value in here
        cipher = ""                                         #created empty list 'cipher'.

        for c in plaintext:   #from here, letters given in the plaintext is one by one taken for further usage.
            if c in alphabet: #checks whether that defined 'c' character is in the list alphabet.
                cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))] #if the 'c' is in the alphabet, it is going to increment by adding the key value.
            else:                                           # I have used MOD in this program to find the shifting value.
                cipher += c                                 #if 'c' is not present in the alphabet, same character will be append to the cipher.
        print("Your Encrypted Message is: ", cipher)        #printing the encrpted massage.

        print()
        print("--------------------------------------")


    elif command == "d":      #this is loop which runs until command = d.
        plaintext = input("Enter Your Message Here: ")      #user should enter a message to decrypt in here.
        alphabet = "abcdefghijklmnopqrstuvwxyz"             #created list 'alphabet' and append letters in the English Alphabet.  
        key = int(input("Enter Your Shifting Value Between 1 and 25: "))    #user should enter the shifting value in here
        cipher = ""                                         #created empty list 'cipher'.

        for c in plaintext:   #from here, letters given in the plaintext is one by one taken for further usage.
            if c in alphabet: #checks whether that defined 'c' character is in the list alphabet.
                cipher += alphabet[(alphabet.index(c)-key)%(len(alphabet))] #if the 'c' is in the alphabet, it is going to increment by subtracting the key value.
            else:                                           # I have used MOD in this program to find the shifting value.
                cipher += c                                 #if 'c' is not present in the alphabet, same character will be append to the cipher.

        print("Your Encrypted Message is: ", cipher)        #printing the decrypted massage.

        print()
        print("--------------------------------------")

    command = input("\nEnter Your Command: ")               #retaking the input when neither d or q not given.








