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

def minimumBribes(q):
    totalDifference = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return

        lowerBound = max(0, q[i]-2)
        for j in range(lowerBound, i):
            if q[j] > q[i]:
                totalDifference += 1

    print(totalDifference)


if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(q)