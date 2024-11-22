def findMinOperations(arr, N, K):
    # Stores number of operations
    operations = 0
 
    # Iterate in the range [0, K-1]
    for i in range(K):
        # Stores frequency of elements
        # separated by distance K
        freq = {}
 
        for j in range(i,N,K):
            if arr[j] in freq:
                freq[arr[j]] += 1
            else:
                freq[arr[j]] = 1
 
        # Stores maximum frequency
        # and corresponding element
        max1 = 0
        num = 0
 
        # Find max frequency element
        # and its frequency
        for key,value in freq.items():
            if (value > max1):
                max1 = value
                num = key
 
        # Update the number of operations
        for key,value in freq.items():
            if (key != num):
                operations += value
 
    # Print the result
    print(operations)

print(findMinOperations([1,3,2,2,3], 5, 3))