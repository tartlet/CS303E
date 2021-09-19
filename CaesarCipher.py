# File: CaesarCipher.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/07/2020
# Date Last Modified: 10/07/2020
# Description of Program: Caesar Cipher program that asks the user if they want to encrypt or decrypt a string. The program
# also recognises illegal commands and can take any case of letters for 'encrypt' and ' decrypt.' Program asks user
# for a shift value which must be between 0 and 25, inclusive. Program then proceeds to utilise a for loop to encrypt/decrypt
# each character in the input string.


command = input("Enter Caesar cipher command (encrypt/decrypt): ")

if command.lower() == 'encrypt':
    print("You've asked to encrypt.")
    shift = eval(input("Please enter shift value (0 .. 25): "))
    if shift < 0 or shift > 25:
        print("Illegal shift value:", str(shift))
        quit()
    fileInput = input("Please enter filename with text to encrypt: ").strip()
    inFile = open(fileInput, "r")
    outNameEnc = "fileInput" + "-enc"
    outFile = open(outNameEnc, "w")
    for ch in inputString:
        if ord(ch) >= 97 and ord(ch) <= 122:
            tempCode = ord(ch)
            newTempCode = tempCode + shift
            if newTempCode > 122:
                wrappedChar = newTempCode - 122 + 96
                newCharacter = chr(wrappedChar)
            else:
                newCharacter = chr(newTempCode)
            print(newCharacter, end = '')
        elif ord(ch) >= 65 and ord(ch) <= 90:
            tempCode = ord(ch)
            newTempCode = tempCode + shift
            if newTempCode > 90:
                wrappedChar = newTempCode - 90 + 89
                newCharacter = chr(wrappedChar)
            else:
                newCharacter = chr(newTempCode)
            print(newCharacter, end = '')
        else: 
            print(ch, end ='')        
elif command.lower() == 'decrypt':
    print("You've asked to decrypt.")
    shift = eval(input("Please enter shift value (0 .. 25): "))
    if shift < 0 or shift > 25:
        print("Illegal shift value:", str(shift))
        quit()
    inputString = input("Please enter text to decrypt: ")
    print("The decrypted text is: ", end ='')
    for ch in inputString:
        if ord(ch) >= 97 and ord(ch) <= 122:
            tempCode = ord(ch)
            newTempCode = tempCode - shift
            if newTempCode < 97:
                wrappedChar = 123 - (97 - newTempCode)
                newCharacter = chr(wrappedChar)
            else:
                newCharacter = chr(newTempCode)
            print(newCharacter, end = '')
        elif ord(ch) >= 65 and ord(ch) <= 90:
            tempCode = ord(ch)
            newTempCode = tempCode - shift
            if newTempCode < 65:
                wrappedChar = 123 - (97 - newTempCode)
                newCharacter = chr(wrappedChar)
            else:
                newCharacter = chr(newTempCode)
            print(newCharacter, end = '')
        else: 
            print(ch, end ='')
else:
    print("Unrecognized command:", command.lower())
    quit()

