# Python program for implementation of Quicksort
# Python program for implementation of Quicksort Sort
"""
// Time Complexity : O(nlogn)
// Space Complexity : O(logn)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None
// Your code here along with comments explaining your approach
Algorithm explanation

Partition
- Choose pivot as last element
- Initialize left = 0
- for i =low to high+1
    - If arr[i] < pivot then swap arr[i] and arr[left]
    - left:=left+1
- Swap arr[left] and arr[pivot]

QuickSortIterative
- To convert the recursive formulation, we use stk to store the start and end 
of the given array
- Apppen (low,high) to stk 
- while stk not empty
    - pop (start,end)
    - pivot <- partition(arr,start,end)
    - if pivot - 1 > start #Consider all the elements which are below pivot
        Append (start,pivot-1) to stk
    - if pivot + 1 < end #Consider all the elements which are above pivot
        Append (pivot+1,end) to stk
"""

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    pivot = h
    left = l
    for i in range(l,h+1):
        if arr[i] < arr[pivot]:
            arr[i],arr[left] = arr[left], arr[i]
            left+=1

    arr[left],arr[pivot] = arr[pivot],arr[left]
    return left


def quickSortIterative(arr, l, h):
    stk = [(l,h)]
    while stk:
        start,end = stk.pop()

        pivot = partition(arr,start,end)

        if pivot - 1 > start:
            stk.append((start,pivot-1))
        if pivot + 1 < end:
            stk.append((pivot+1,end))

arr = [10, 7, 8, 9, 1, 5] 
arr = [10, 30, 20, 15, 23, 12]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 