import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    
    numberOfMoves = 0
    currentHeight = m
    while(currentHeight > 1):
        lastHeight = currentHeight
        for i in range(currentHeight, 0, -1):
            if currentHeight % i == 0:
                currentHeight = i
                numberOfMoves += 1
                break
        if lastHeight == currentHeight:
            break
    
    numberOfMoves *= n
    
    if numberOfMoves % 2 == 1:
        return 1
    return 2


if __name__ == '__main__':
    n = 2
    m = 6
    result = towerBreakers(n, m)
    print(result)