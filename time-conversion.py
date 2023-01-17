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
#

def timeConversion(s):
    # Write your code here
    if s[-2:] == "AM":
        return convertAM(s)

    return convertPM(s)


def convertAM(s):
    if s[0:2] == "12":
        s = f"00{s[2:]}"
    
    return s[0:-2]


def convertPM(s):
    hour = int(s[0:2])
    if hour != 12:
        hour += 12

    return f"{hour}{s[2:-2]}"


if __name__ == '__main__':
    s = "12:40:22AM"

    result = timeConversion(s)
    print(result)
