# Encoder / Decoder

This repository contains three files, an encoder, a decoder, and an accompanying JSON file which holds a list of characters that have been enumerated.

## Encoding

The encoding is done by iterating over each character in a file, and converting it to the binary form of the corresponding integer in the JSON file.

It also allows the input of a string, which will add the string length to the integer before it is converted to binary. An empty input can also just be given instead. A limitation of this is that only the length of the string needs to be matched to decode again.

The program checks for the location of the file to encode. It will look for a file in a folder called "Encrypt File". If the folder is not present, it will create it, and the file will be able to be placed there before continuing the program.

## Decoding

The decoding program works in reverse of the encoding. It reads the encoded file, and pulls the individual binary numbers out of it. The binary numbers are then converted to integers, a string length subtracted from them, and then the corresponding characters from the JSON file are written over them in the encoded file. If a string was inputted when encoding, the string must also be inputted when this program is ran.

The presence of a file to encode is checked, and prints a message to notify if there is no file. The file contents are also checked to make sure it is an encoded file. It should only contain 0s and 1s.