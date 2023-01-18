import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length = len(arr)

    if length == 0:
        return

    positive = 0
    negative = 0
    zero = 0
    
    for val in arr:
        if val > 0:
            positive += 1
        elif val < 0:
            negative += 1
        else:
            zero += 1

    print(round(positive / length, 6))
    print(round(negative / length, 6))
    print(round(zero / length, 6))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
