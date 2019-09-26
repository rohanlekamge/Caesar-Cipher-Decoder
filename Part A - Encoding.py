#Part A: Encoding


plaintext = input("\nEnter Your Message Here: ")    #user should enter a message to encrypt in here
alphabet = "abcdefghijklmnopqrstuvwxyz"                 
key = int(input("\nEnter Your Shifting Value Between 1 and 25: "))  #user should enter the shifting value in here
cipher = ""

for c in plaintext:
    if c in alphabet:
        cipher += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
    else:                                           #cipher is just a variable
        cipher += c                                 #I have used MOD in this program to find the shifting value
print("\nYour Encrypted Message is: ", cipher)
print()
print("--------------------------------------")
