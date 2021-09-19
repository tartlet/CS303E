#  File: Palindrome.py

#  Description: Given a string, make the smallest palindrome by
#  adding characters to the front of the string

#  Student Name: Jingsi Zhou

#  Student UT EID: jz24729

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

def isPalindrome(s):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
   if len(s) <= 1:
        return True
   elif s[0] != s[len(s)- 1]:
        return False
   else:
        return isPalindrome(s[1:len(s)-1])

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    is_pal = False
    i = len(str)
    while is_pal == False:
        s = str[0:i]
        is_pal = isPalindrome(s)
        if is_pal == True:
            break
        i -= 1
    print(s)
    # s is the palindrome
    diff = str[i + 1:]
    # reverse the string 
    rev = diff[-1::-1]
    return rev + str


def main():
    user_input = sys.stdin.readline()   
    while user_input != '':
        print(user_input)
        if isPalindrome(user_input):
            print(user_input)
        else:
            print(makePalindrome(user_input))
            

