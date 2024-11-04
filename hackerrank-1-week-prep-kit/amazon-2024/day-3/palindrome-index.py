#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def isPalindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    # Write your code here
    print(s)
    n = len(s)
    if n == 1:
        return -1
    
    for i in range(n):
        j = n - (i + 1)
        if j <= i:
            return -1
        
        if s[i] == s[j]:
            continue
        
        if s[i] == s[j-1] and isPalindrome(f'{s[:j]}{s[j+1:]}'):
            return j
        if s[i+1] == s[j] and isPalindrome(f'{s[:i]}{s[i+1:]}'):
            return i
        
        return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
