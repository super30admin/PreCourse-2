
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    p = arr[h]
    small_index = l-1   # small element index

    for i in range(l, h):
        # when current elem is <= point of partition
        if arr[i] <= p:
            small_index+=1
            arr[small_index], arr[i] = arr[i], arr[small_index]

    arr[small_index + 1], arr[h] = arr[h], arr[small_index + 1]
    return (i + 1)

def quickSortIterative(arr, l, h):
    #write your code here
    if l<h:
        index = partition(arr, l, h)
 
        quickSortIterative(arr, l, index-1)
        quickSortIterative(arr, index + 1, h)
 
arr = [41, 21, 16, 9, 5]
quickSortIterative(arr, 0, len(arr) - 1)
print("sorted arr: ",arr)