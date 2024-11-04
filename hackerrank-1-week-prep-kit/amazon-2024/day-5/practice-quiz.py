#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    match_dict = {}
    for num in arr:
        if num > k:
            match = num - k
        else:
            match = k - num
            
        if match in match_dict:
            match_dict[match] += 1
        else:
            match_dict[match] = 0
            
    return sum(match_dict.values())


print(pairs(2, [1,5,3,4,2]))