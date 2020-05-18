# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        smallest = arr[i]
        j = i
        while j < len(arr) - 1:
            if smallest > arr[j+1]:
                smallest = arr[j+1]
                arr[i], arr[j+1] = arr[j+1], arr[i]
                j += 1
            else:
                j +=1

        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    j = len(arr) - 1

    while j > 0:
        
        for i in range(j):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] =  arr[i], arr[i+1]
            
        j -= 1


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
