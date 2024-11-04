#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion

def handleAm(s):
    if s.startswith('12'):
        return f'00{s[2:]}'
    
    return s
    
def handlePm(s):
    if s.startswith('12'):
        return s
    
    hour = int(s[:2])
    return f'{hour+12}{s[2:]}'
    

def timeConversion(s):
    time = s[:-2]
    amPm = s[-2:]
    
    if amPm == 'AM':
        return handleAm(time)
    return handlePm(time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
