#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    wordDict = {}
    for word in words:
        st = word[0]
        ed = word[1:]
        
        if st not in wordDict:
            wordDict[st] = [ed]
            continue
        
        for potential in wordDict[st]:
            #print(potential, ed)
            if ed.startswith(potential):
                print('BAD SET')
                print(word)
                return
            if potential.startswith(ed):
                print('BAD SET')
                print(st+ed)
                return
        
        wordDict[st].append(ed)
    
    print('GOOD SET')

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
