#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
def getSortedString(s):
    return ''.join(sorted(s))

def isSorted(arr):
    x = arr[:]
    x = getSortedString(x)
    return x == arr

def getColumn(grid, index):
    column = ''
    for row in grid:
        column += row[index]
    return column

def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i] = getSortedString(grid[i])
    
    for j in range(len(grid[0])):
        column = getColumn(grid, j)
        if not isSorted(column):
            return 'NO'
    
    return 'YES'
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
