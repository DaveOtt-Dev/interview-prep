#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

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
    i = 0
    
    heapq.heapify(A)
    
    while len(A) > 1:
        # when all cookies are sweet enough, we return
        if A[0] >= k:
            return i

        least_sweet_cookie = heapq.heappop(A)
        second_least_sweet_cookie = heapq.heappop(A)
        
        new_cookie = least_sweet_cookie + (2 * second_least_sweet_cookie)
        
        heapq.heappush(A, new_cookie)
        i += 1
    
    if sum(A) < k:
        return -1
    return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
