#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer

def lonelyinteger(a):
    # Write your code here
    if len(a) == 1:
        return a[0]
    
    numDict = {}
    
    for num in a:
        if num in numDict:
            numDict[num] += 1
        else:
            numDict[num] = 1
    
    for num in numDict:
        if numDict[num] == 1:
            return num
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
