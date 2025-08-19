# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high): 
    #write your code here
    pivot = arr[low]
    i = low+1
    j = high
    
    while True:
        while i<=high and arr[i] <= pivot: 
            i+=1
        while j >= low and arr[j] > pivot: 
            j-=1
        if i >= j: 
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quickSortIterative(arr, l, h):
  #write your code here
    stack = [(l, h)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        p = partition(arr, low, high)
        stack.append((low, p - 1))
        stack.append((p + 1, high))
    
# arr = [10, 7, 8, 9, 1, 5]
# quickSortIterative(arr, 0, len(arr) - 1)
# print(arr)