def flippingMatrix(matrix):
    # Write your code here
    rowColLength = len(matrix)
    if rowColLength == 0:
        return 0
    
    largestSum = 0
    lastIndex = rowColLength - 1
        
    for i in range(rowColLength // 2):
        for j in range(rowColLength // 2):
            num1 = matrix[i][j]
            num2 = matrix[i][lastIndex-j]
            num3 = matrix[lastIndex-i][j]
            num4 = matrix[lastIndex-i][lastIndex-j]

            arr = [num1, num2, num3, num4]

            candidate = max(arr)
            largestSum += candidate
        
    return largestSum


if __name__ == '__main__':
    matrix = [
        [112,42,83,119],
        [56,125,56,49],
        [15,78,101,43],
        [62,98,114,108]
    ]

    result = flippingMatrix(matrix)
    print(result)