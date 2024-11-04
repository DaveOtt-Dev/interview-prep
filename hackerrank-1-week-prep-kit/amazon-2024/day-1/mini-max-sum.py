#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    
    mins = arr[:4]
    maxs = arr[-4:]
    
    print(f'{sum(mins)} {sum(maxs)}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)