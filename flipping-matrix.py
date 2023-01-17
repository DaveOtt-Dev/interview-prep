def flippingMatrix(matrix):
    # Write your code here
    
    worstRowOrCol = getWorstRowOrCol(matrix)

    while worstRowOrCol is not None:
        rowOrCol = worstRowOrCol[0]
        index = worstRowOrCol[1]
        arr = worstRowOrCol[2]

        if rowOrCol == "row":
            matrix[index] = arr[::-1]
        else:
            revCol = getReverseColumn(matrix, index)
            for i in range(len(matrix)):
                matrix[i][index] = revCol[i]

        worstRowOrCol = getWorstRowOrCol(matrix)
    
    print(matrix)
    return getTopLeftSum(matrix)
    

def getWorstRowOrCol(matrix):
    difference = 0
    isRow = None
    index = None
    arr = None

    length = len(matrix[0])
    for i in range(length):
        row = matrix[i]

        left = row[0:int(length/2)]
        right = row[int(length/2):]

        rowDiff = sum(right) - sum(left)
        if rowDiff > difference:
            difference = rowDiff
            isRow = True
            index = i
            arr = row

    length = len(matrix)
    for i in range(len(matrix[0])):
        col = getColumn(matrix, i)

        top = col[0:int(length/2)]
        bot = col[int(length/2):]

        colDiff = sum(bot) - sum(top)
        if colDiff > difference:
            difference = colDiff
            isRow = False
            index = i
            arr = col

    if arr == None:
        return None

    if isRow:
        return ("row", index, arr)

    return ("col", index, arr)



def getColumn(matrix, index):
    column = []
    for row in matrix:
        column.append(row[index])
    return column


def getReverseColumn(matrix, index):
    column = []
    for row in matrix:
        column.append(row[index])
    return column[::-1]


def getTopLeftSum(matrix):
    answer = 0
    rowLen = len(matrix[0])
    colLen = len(matrix)

    for i in range(int(colLen / 2)):
        answer += sum(matrix[i][0: int(rowLen/2)])

    return answer


if __name__ == '__main__':
    matrix = [
        [112,42,83,119],
        [56,125,56,49],
        [15,78,101,43],
        [62,98,114,108]
    ]

    result = flippingMatrix(matrix)
    print(result)