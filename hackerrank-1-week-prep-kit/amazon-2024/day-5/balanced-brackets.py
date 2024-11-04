#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    opening_brackets = ['(', '{', '[']
    bracket_dict = { ')': '(', '}': '{', ']': '[' }
    stack = []
    
    for c in s:
        if c in opening_brackets:
            stack.append(c)
            continue
            
        if len(stack) == 0:
            return 'NO'
            
        if bracket_dict[c] != stack.pop():
            return 'NO'

    if len(stack) != 0:
        return 'NO'
    return 'YES'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
