#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
def minimumBribesHelper(q):
    bribeCount = 0
    for i in range(len(q)):
        for j in range(max(0, q[i] - 2), i):
            if q[j] - (j+1) > 2:
                return 'Too chaotic'
            if q[j] > q[i]:
                bribeCount += 1
    return bribeCount

def minimumBribes(q):
    print(minimumBribesHelper(q))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
