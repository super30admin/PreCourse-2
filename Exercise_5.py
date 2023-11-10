# Python program for implementation of Quicksort
from collections import deque
 
def swap (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
# This function is same in both iterative and recursive
def partition(a, start, end):

    pivot = a[end]
 
    pIndex = start

    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1
 
   
    swap(a, pIndex, end)
 
    return pIndex

def quickSortIterative(arr):
  #write your code here
    stack = deque()
 
    start = 0
    end = len(a) - 1

    stack.append((start, end))
   
    while stack:
        start, end = stack.pop()
 
       
        pivot = partition(a, start, end)
 
      
        if pivot - 1 > start:
            stack.append((start, pivot - 1))
 
       
        if pivot + 1 < end:
            stack.append((pivot + 1, end))

# Iterative Implementation of Quicksort
if __name__ == '__main__':
 
    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
 
    quickSortIterative(a)
 
    # print the sorted list
    print(a)