def pairs(k, arr):
    # Write your code here
    mySet = set(arr)
            
    numPairs = 0
    for val in mySet:
        otherVal = val - k
        if otherVal in mySet:
            numPairs += 1
    
    return numPairs