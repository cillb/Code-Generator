"""
This program encrypts a message contained in a specified folder. The program encrypts the message
taking an integer that corresponds to a character contained in encryption.json, adds a modifier
to the integer, then converts it to binary. The binary string replaces the original character 
and is written into the message file. The characters that are encrypted are upper and lowercase 
letters, and the special characters: ( ) ' , . ? !
"""
from json import load
from os import mkdir, chdir, listdir

# enter the folder location of the encryption/decryption programs, and the encryption.json file
chdir()# enter location where these programs and accompanying json file are kept

# enter a string to use as a modifier 
modifier = len(input("Please enter your encryption modifier:\t"))

# store the code as a py object
with open("encryption.json", "r") as enc:
    encryption = load(enc)

# check if the folder that contains your message is present
if "Encrypt File" not in listdir():
    mkdir("Encrypt File")
    print("Please place the file containing your message into the folder: Encrypt File")
chdir("Encrypt File")
filesinfolder = listdir()
if not filesinfolder:# check if the message file is present
    print("No file to encrypt present.")
    exit()

file = filesinfolder[0]
with open(file, "r") as mess:
    message = mess.read()# store the message as a py object

# iterate through each character in the message, and encrypt it as it corresponds to the code
for m in message:
    k = message.index(m)
    for e in encryption:
        if m == e[1]:
            message = message.replace(message[k], bin(e[0]+modifier)[2:].zfill(8), 1)# the binary object in python normally reads as 0b1011, this is modified to read as an 8 bit binary number, ie 00001011
            break

with open(file, "w") as mess:
    mess.write(message)
