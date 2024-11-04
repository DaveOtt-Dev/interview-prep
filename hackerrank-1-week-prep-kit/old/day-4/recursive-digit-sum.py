import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    stringSum = getStringSum(n)
    stringSum *= k

    if stringSum > 9:
        return superDigit(str(stringSum), 1)

    return stringSum
    

def getStringSum(n):
    total = 0
    for char in n:
        total += int(char)
    return total


if __name__ == '__main__':

    k = int(4)
    n = "9875"

    result = superDigit(n, k)
    print(result)