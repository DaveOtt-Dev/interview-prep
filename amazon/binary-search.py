
def binary_search(arr, val):
    return binary_search_helper(arr, val, 0)

def binary_search_helper(arr, val, offset):
    if not arr:
        return -1
    
    middle = len(arr) // 2

    if arr[middle] > val:
        return binary_search_helper(arr[:middle], val, offset)
    if arr[middle] < val:
        return binary_search_helper(arr[middle:], val, middle + offset)

    return middle + offset


print(binary_search([0,2,4,5,6,7,8,9,10,12,14], 5))
print(binary_search([0,2,4,5,6,7,8,9,10,12,14], 10))
print(binary_search([0,2,4,5,6,7,8,9,10,12,14], 0))
print(binary_search([0,2,4,5,6,7,8,9,10,12,14], 14))