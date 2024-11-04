import math
import os
import random
import re
import sys
from heapq import heapify, heappop, heappush

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    heapify(A)
    
    count = 0
    while A[0] < k:
        if len(A) < 2:
            return -1
            
        val = heappop(A) + 2 * heappop(A)
        heappush(A, val)
        count += 1
    
    return count
    
    
if __name__ == '__main__':
    k = 9
    A = [1,2,99,99,6,7,6]
    result = cookies(k, A)
    print(result)
