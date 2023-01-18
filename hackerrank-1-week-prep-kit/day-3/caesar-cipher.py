import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

minUppercase = 65
maxUppercase = 90

minLowercase = 97
maxLowercase = 122

def caesarCipher(s, k):
    # Write your code here
    cipherString = ""
    for char in s:
        cipherString += caesarCipherCharacter(char, k)
    
    return cipherString


def caesarCipherCharacter(char, k):
    charInt = ord(char)
    
    if (charInt < minUppercase or charInt > maxUppercase) and (charInt < minLowercase or charInt > maxLowercase):
        return char

    alphabetLength = 26

    if char.islower():
        return chr((((charInt - minLowercase) + k) % alphabetLength) + minLowercase)

    return chr((((charInt - minUppercase) + k) % alphabetLength) + minUppercase)


if __name__ == '__main__':
    s = "www.abc.xy"
    k = 87

    result = caesarCipher(s, k)
    print(result)