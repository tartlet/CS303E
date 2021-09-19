# File: MyStringFunctions.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
# 
# Date Created: 10/30/2020
# Date Last Modified: 10/30/2020
# Description of Program: Program contains multiple functions that can carry out a 
# variety of different operations on an input string.

def myAppend(string, ch):
    # Return a new string that is like str but with 
    # character ch added at the end
    return string + ch

def myCount(string, ch):
    # Return the number of times character ch appears
    # in str.
    count = 0
    for i in string:
        if i == ch:
            count += 1
    return count

def myExtend(str1, str2):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    newstr = str1 + str2
    return newstr

def myMin(string):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if string == "":
        print("Empty string: no min value")
        return None
    else:
        firstCode = ord(string[0])
        for i in string:
            code = ord(i)
            if code < firstCode:
                firstCode = code
        return chr(firstCode)
                
def myInsert(str, i, ch):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if i > len(str):
        print("Invalid index")
        return None
    else:
        temp = str[i: ]
        newstr = str[ :i] + ch
        newnewstr = newstr + temp
        return newnewstr
        
def myPop(str, i):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    if i >= len(str):
        print("Invalid index")
        return (str, None)
    else:
        str1 = str[:i]
        str2 = str[i+1:]
        newstr = str1 + str2
        return (newstr, str[i])
        

def myFind(string, ch):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    for i in range(0,len(string)):
        if string[i] == ch:
            return i
    return -1
    
def myRFind(str, ch):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    count = 0
    for i in range(0, len(str)):
        if str[i] != ch:
            count += 1
    if count == len(str):
        return -1 
    else: 
        for i in range(0, len(str)):
            if str[i] == ch:
                temp = i
        return i 
    
def myRemove(str, ch):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.
    for i in range(0, len(str)):
        if str[i] == ch:
            newstr = str[:i] + str[i+1:]
            return newstr
    return str
    
def myRemoveAll(string, ch):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    count = 0
    for i in range(0, len(string)):
        if string[i] != ch:
            count = count + 1
    if count == len(string):
        return string
    else: 
        temp = []
        for i in range(0, len(string)):
            if string[i] == ch:
                temp.append(i)
        #REVERSE TEMP!
        newtemp = []
        for i in range(0, len(temp)):
            tempvar = temp[len(temp)-1-i]
            newtemp.append(tempvar)
        for i in range(0, len(newtemp)):
            removethis = newtemp[i]
            newstr1 = string[:removethis]
            newstr2 = string[removethis + 1:]
            string = newstr1 + newstr2 
        return string
        

def myReverse(str):
    # Return a new string like str but with the characters
    # in the reverse order. 
    newstr = ''
    for i in range(0,len(str)):
        temp = str[len(str)-1-i]
        newstr = newstr + temp
    return newstr  