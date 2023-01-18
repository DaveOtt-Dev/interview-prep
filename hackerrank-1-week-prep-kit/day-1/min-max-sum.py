import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minVal = min(arr)
    maxVal = max(arr)
    
    minArr = arr[:]
    minArr.remove(maxVal)
    
    maxArr = arr[:]
    maxArr.remove(minVal)
    
    print(f"{sum(minArr)} {sum(maxArr)}")
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)