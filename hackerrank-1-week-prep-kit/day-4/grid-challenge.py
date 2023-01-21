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

def gridChallenge(grid):
    # Write your code here
    grid = sortGridRows(grid)
    return isGridColsAlphabetic(grid)
    
def sortGridRows(grid):
    for i in range(len(grid)):
        row = grid[i]
        rowArray = row.replace("", " ").split(" ")
        rowArray.sort()
        grid[i] = "".join((e) for e in rowArray)

    return grid
    

def isGridColsAlphabetic(grid):
    for i in range(len(grid[0])):
        column = getColumn(grid, i)
        if not isAscending(column):
            return "NO"
    return "YES"


def getColumn(grid, index):
    column = []
    for row in grid:
        column.append(row[index])
    return column


def isAscending(array):
    previous = array[0]
    for val in array:
        if val < previous:
            return False
        previous = val
    return True
    

if __name__ == '__main__':
    grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    result = gridChallenge(grid)
    print(result)