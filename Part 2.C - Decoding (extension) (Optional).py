#Part C: Decoding (Extension)

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
        hint = input("Enter First Word Here: ")             #enter the first word of the sentence to crack the code
        if plaintext[0] in alphabet:
            first = plaintext[0]        #taking the index of the first letter from the plaintext.
        elif plaintext[1] in alphabet:
            first = plaintext[1]        #taking the index of the second letter from the plaintext.
        elif plaintext[2] in alphabet:
            first = plaintext[2]        #taking the index of the third letter from the plaintext.
        elif plaintext[3] in alphabet:
            first = plaintext[3]        #taking the index of the fourth letter from the plaintext.
        elif plaintext[4] in alphabet:
            first = plaintext[4]        #taking the index of the fifth letter from the plaintext.
        elif plaintext[5] in alphabet:
            first = plaintext[5]        #taking the index of the sixth letter from the plaintext.
            
        if hint[0] in alphabet:
            second = hint[0]            #taking the index of the first letter from the hint.
        elif hint[1] in alphabet:
            second = hint[1]            #taking the index of the second letter from the hint.
        elif hint[2] in alphabet:
            second = hint[2]            #taking the index of the third letter from the hint.
        elif hint[3] in alphabet:
            second = hint[3]            #taking the index of the fourth letter from the hint.
        elif hint[4] in alphabet:
            second = hint[4]            #taking the index of the fifth letter from the hint.
        elif hint[5] in alphabet:
            second = hint[5]            #taking the index of the sixth letter from the hint.
            
        key1 = plaintext.index(first) - alphabet.index(first)   #checking the encryptes massage, for the key value, according to the alphabet.
        key2 = hint.index(second) - alphabet.index(second)      #checking the hint, for the key value, according to the alphabet.
        key = key2 - key1           #finding the real key value.
        cipher = ""     #I have used arrays in this program

        for c in plaintext:   #from here, letters given in the plaintext is one by one taken for further usage.
            if c in alphabet: #checks whether that defined 'c' character is in the list alphabet.
                cipher += alphabet[(alphabet.index(c)-key)%(len(alphabet))] #if the 'c' is in the alphabet, it is going to increment by subtracting the key value.
            else:                                           # I have used MOD in this program to find the shifting value.
                cipher += c                                 #if 'c' is not present in the alphabet, same character will be append to the cipher.

        print("Your Decrypted Message is: ", cipher)        #printing the decrypted massage.
        print("Shifting Value is",key)                      #print the identified shifting key value.
        print()
        print("--------------------------------------")

    command = input("\nEnter Your Command: ")               #retaking the input when neither d or q not given.










