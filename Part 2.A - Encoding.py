#Part A: Encoding


plaintext = input("\nEnter Your Message Here: ")    #user should enter a message to encrypt in here.
alphabet = "abcdefghijklmnopqrstuvwxyz"             #created list 'alphabet' and append letters in the English Alphabet.
key = -1
while key < 0 or key > 25:
    key = int(input("\nEnter Your Shifting Value Between 1 and 25: "))  #user should enter the shifting value in here.
cipher = ""                                         #created empty list 'cipher'.

for c in plaintext:   #from here, letters given in the plaintext is one by one taken for further usage.
    if c in alphabet: #checks whether that defined 'c' character is in the list alphabet.
        cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))] #if the 'c' is in the alphabet, it is going to increment by adding the key value.
    else:                                           # I have used MOD in this program to find the shifting value.
        cipher += c                                 #if 'c' is not present in the alphabet, same character will be append to the cipher.
print("\nYour Encrypted Message is: ", cipher)      #printing the encrpted massage.
print()
print("--------------------------------------")
