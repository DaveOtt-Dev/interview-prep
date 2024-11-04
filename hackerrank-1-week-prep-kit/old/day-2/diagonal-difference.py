import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    leftToRight = 0
    rightToLeft = 0

    arrLength = len(arr)
    
    j = arrLength - 1
    for i in range(arrLength):
        leftToRight += arr[i][i]
        rightToLeft += arr[i][j-i]
        
    return abs(leftToRight - rightToLeft)
    
    
if __name__ == '__main__':
    arr = [
        [11,2,4],
        [4,5,6],
        [10,8,-12]
    ]

    result = diagonalDifference(arr)
    print(result)