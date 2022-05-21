# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = l
    j = h - 1
    pivot = arr[h]
    while i < j:
        while i < h and arr[i] < pivot:
            i += 1
        while j > l and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[h] = arr[h], arr[i]
    return i
  #write your code here


def quickSortIterative(arr, l, h):
    stackSize = h - l + 1
    stack = [0] * (stackSize)
    top = -1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = partition(arr, l, h)
        if p-1 > l:
            top += 1
            stack[top] = 1
            top += 1
            stack[top] = p-1

        if p+1 < h:
            top += 1
            stack[top] = p+1
            top += 1
            stack[top] = h


  #write your code here
arr = [10, 7, 8, 9, 1, 5]
quickSortIterative(arr, 0, len(arr)-1)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
#Time complexity : O(n^2)
#Space complexity: O(n); stack is used additionly