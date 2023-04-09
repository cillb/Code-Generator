"""
This program encodes a message contained in a specified folder. The program encodes the message
taking an integer that corresponds to a character contained in encoding.json, adds a modifier
to the integer, then converts it to binary. The binary string replaces the original character 
and is written into the message file. The characters that are Encodeed are upper and lowercase 
letters, and the special characters: ( ) ' , . ? !
"""
from json import load
from os import mkdir, chdir, listdir

# enter the folder location of the encoding/decryption programs, and the encoding.json file
#chdir()# enter location where these programs and accompanying json file are kept

# enter a string to use as a modifier 
modifier = len(input("Please enter your encoding modifier:\t"))

# store the code as a py object
with open("encoding.json", "r") as enc:
    encoding = load(enc)

# check if the folder that contains your message is present
if "Encode File" not in listdir():
    mkdir("Encode File")
    print("Please place the file containing your message into the folder: Encode File")
chdir("Encode File")
filesinfolder = listdir()
if not filesinfolder:# check if the message file is present
    print("No file to encode present.")
    exit()

file = filesinfolder[0]
with open(file, "r") as mess:
    message = mess.read()# store the message as a py object

# iterate through each character in the message, and encode it as it corresponds to the code
for m in message:
    k = message.index(m)
    for e in encoding:
        if m == e[1]:
            message = message.replace(message[k], bin(e[0]+modifier)[2:].zfill(8), 1)# the binary object in python normally reads as 0b1011, this is modified to read as an 8 bit binary number, ie 00001011
            break

with open(file, "w") as mess:
    mess.write(message)
