# Python program for implementation of Quicksort
#Time Complexity :  O(nlogn)
#Space Complexity : O(n)
from collections import deque
# This function is same in both iterative and recursive
def partition(arr,low,high):
    
    pivot = high

    i = low
    j= low
    while i < high:
        if arr[i] < arr[pivot]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i+1
            j = j+1
        else:
            i = i+1
    temp = arr[pivot]
    arr[pivot] = arr[j]
    arr[j] = temp
    return j
  


def quickSortIterative(arr, low, high):
    stack = deque()
    # push the l and h index of the array into the stack
    stack.append((low, high))
    while stack:
        low, high = stack.pop()
        print(low,high)
        p = partition(arr,low,high)
        if p-1>low:
            stack.append((low, p-1))
        if p+1 < high:
            stack.append((p+1, high))
    # return arr


arr = [10,11, 7, 8, 9,2, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 