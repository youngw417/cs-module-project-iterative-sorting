def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] is target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) is 0:
        return -1

    left = 0
    right = len(arr) - 1
   

    while right >=  left:
        middle =  (left + right) // 2
        if target == arr[middle]:
            return middle
        if target > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1  


    return -1  # not found
