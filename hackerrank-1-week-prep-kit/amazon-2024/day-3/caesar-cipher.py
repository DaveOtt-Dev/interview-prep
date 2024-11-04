#!/bin/python3

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

def getEncryptedChar(c, k):
    # uppercase
    if ord(c) > 64 and ord(c) < 91:
        new = ord(c) + k
        while new > 90:
            new -= 26
        return chr(new)
    # lowercase
    if ord(c) > 96 and ord(c) < 123:
        new = ord(c) + k
        while new > 122:
            new -= 26
        return chr(new)
    # not a charcter in the alphabet
    return c

def caesarCipher(s, k):
    # Write your code here
    output = ''
    for c in s:
        output += getEncryptedChar(c, k)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
