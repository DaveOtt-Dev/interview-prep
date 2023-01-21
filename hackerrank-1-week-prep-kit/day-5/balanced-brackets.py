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
    stack = []
    
    for c in s:
        if isOpeningBracket(c):
            stack.append(c)
            continue

        if len(stack) == 0:
            return "NO"
        
        x = stack.pop()
        if getClosingBracket(x) != c:
            return "NO"
            
    if len(stack) != 0:
        return "NO"
    return "YES"
    
    
def isOpeningBracket(c):
    return c == "(" or c == "{" or c == "["


def getClosingBracket(c):
    if c == "(":
        return ")"
    if c == "{":
        return "}"
    if c == "[":
        return "]"
    return
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()