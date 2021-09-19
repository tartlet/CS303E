# File: CaesarCipherFile.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/13/2020
# Date Last Modified: 11/13/2020
# Description of Program: Caesar Cipher program that asks the user if they want to encrypt or decrypt a text file. The program
# also recognises illegal commands and can take any case of letters for 'encrypt' and ' decrypt.' Program asks user
# for a shift value which must be between 0 and 25, inclusive. Program then proceeds to utilise a for loop to encrypt/decrypt
# each character in the input file.


command = input("Enter Caesar cipher command (encrypt/decrypt): ")

if command.lower() == 'encrypt':
    print("You've asked to encrypt.")
    shift = eval(input("Please enter shift value (0 .. 25): "))
    if shift < 0 or shift > 25:
        print("Illegal shift value:", str(shift))
        quit()
    fileInput = input("Please enter filename with text to encrypt: ")
    inFile = open(actualInput, "r")
    outName = fileInput + "-Enc"
    outNameEnc = fileInput + "-Enc" + ".txt"
    outFile = open(outNameEnc, "w")
    print("The input filename is", fileInput)
    for line in inFile:
        for ch in line:
            if ord(ch) >= 97 and ord(ch) <= 122:
                tempCode = ord(ch)
                newTempCode = tempCode + shift
                if newTempCode > 122:
                    wrappedChar = newTempCode - 122 + 96
                    newCharacter = chr(wrappedChar)
                else:
                    newCharacter = chr(newTempCode)
                outFile.write(newCharacter)
            elif ord(ch) >= 65 and ord(ch) <= 90:
                tempCode = ord(ch)
                newTempCode = tempCode + shift
                if newTempCode > 90:
                    wrappedChar = newTempCode - 90 + 89
                    newCharacter = chr(wrappedChar)
                else:
                    newCharacter = chr(newTempCode)
                outFile.write(newCharacter)
            else: 
                outFile.write(ch)
    print("The output filename is", outName)
    
elif command.lower() == 'decrypt':
    print("You've asked to decrypt.")
    shift = eval(input("Please enter shift value (0 .. 25): "))
    if shift < 0 or shift > 25:
        print("Illegal shift value:", str(shift))
        quit()
    fileInput = input("Please enter filename with text to decrypt: ")
    actualInput = fileInput + ".txt"
    inFile = open(actualInput, "r")
    outName = fileInput + "-Dec"
    outNameDec = fileInput + "-Dec" + ".txt"
    outFile = open(outNameDec, "w")
    print("The input filename is", fileInput)
    for line in inFile:
        for ch in line:
            if ord(ch) >= 97 and ord(ch) <= 122:
                tempCode = ord(ch)
                newTempCode = tempCode - shift
                if newTempCode < 97:
                    wrappedChar = 123 - (97 - newTempCode)
                    newCharacter = chr(wrappedChar)
                else:
                    newCharacter = chr(newTempCode)
                outFile.write(newCharacter)
            elif ord(ch) >= 65 and ord(ch) <= 90:
                tempCode = ord(ch)
                newTempCode = tempCode - shift
                if newTempCode < 65:
                    wrappedChar = 123 - (97 - newTempCode)
                    newCharacter = chr(wrappedChar)
                else:
                    newCharacter = chr(newTempCode)
                outFile.write(newCharacter)
            else: 
                outFile.write(ch)
    print("The output filename is", outName)
else:
    print("Unrecognized command:", command.lower())
    quit()

