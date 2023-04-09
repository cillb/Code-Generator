"""
This program decodes the message previously changed by the accompanying Encode program. The program 
decodes the message by extracting each 8 bit binary string, converting it to an integer and subtracting
the modifier used in the initial encoding. Then the corresponding characters for each integer are 
written onto the message.
"""
from json import load
from os import chdir, listdir

# enter the folder location of the encoding/decoding programs, and the encoding.json file
#chdir()# enter the location where these programs and accompanying json file are kept

# enter the string needed for the modifier
modifier = len(input("Please enter your encoding modifier:\t"))

# store the code as a py object
with open("encoding.json", "r") as enc:
    encoding = load(enc)

# check if the folder containing the message is present
if "Encode File" not in listdir():
    print("The folder is not present.")
    exit()
chdir("Encode File")
filesinfolder = listdir()
file = filesinfolder[0]
with open(file, "r") as mess:# store the message as a py object
    message = mess.read()
# remove spacing and newlines from the message as a new string object
tempmess = message.replace(" ", "")
tempmess = tempmess.replace("\n", "")

# check if the file is encoded
for io in tempmess:
    if not (io == "1" or io == "0"):
        print(io)
        print("The file is not an encoded file.")
        exit()

# extract the individual binary strings
decoding = [tempmess[m*8:(m+1)*8] for m in range(int(len(tempmess)/8))]
decod = [(int(decoding[d], 2) - modifier) for d in range(len(decoding))]# the binary number is converted back to integer
for i in range(len(decod)):
    for j in encoding:
        if decod[i] == j[0]:
            message = message.replace(decoding[i], j[1], 1)
            break
# write the decoded message to the file
with open(file,"w") as mess:
    mess.write(message)
