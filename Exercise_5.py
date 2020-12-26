# Python program for implementation of Quicksort
# Idea is to store starting and ending indexes for usage during processing instead of recursion. This will save extra space required for recursion
# Same as partition of recursive quicksort
def partition(arr,low,high):
    i = low+1
    j = high
    pivot = arr[low]
    while(i<=j):
        while(arr[i]<pivot and i<high):
            i = i+1
        while(arr[j]>pivot):
            j = j-1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i = i+1
            j = j-1
        else:
            i = i+1
    arr[low] = arr[j]
    arr[j] = pivot
    return j

def quickSortIterative(arr, l, h):
    # stack for storing sublist start and end index
    stack = []
    # get starting and ending index of given list (vector)
    start = l
    end = h
    # push list start and end index to the stack
    stack.append((start, end))
    # loop till stack is empty
    while stack:
        # pop top pair from the list and get sub-list starting
        # and ending indices
        start, end = stack.pop()
        # rearrange the elements across pivot
        pivot = partition(arr, start, end)
        # push sub-list indices containing elements that are
        # less than current pivot to stack
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
        # push sub-list indices containing elements that are
        # more than current pivot to stack
        if pivot + 1 < end:
            stack.append((pivot + 1, end))

# Code to print the list 
def printList(arr): 
  print(arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    n = len(arr)
    print ("Given array is", end="\n")  
    printList(arr) 
    quickSortIterative(arr, 0, n-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 