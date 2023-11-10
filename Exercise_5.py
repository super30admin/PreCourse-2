import random
from collections import deque
"""
Quick Sort:
we will take a stack and append the low and high values, we will pop them till stack is empty. We will chose return
the pivot element from the partition by taking last value of the array as the pivotand rearranging all the values depending
if they are greater or lesser than the pivot
We will have a border value, everything to the left of the border will be smaller than the pivot
is the current number in consideration smaller than the pivot, if yes we will swap the value with the border
and then we advance both pointers i.e border and the current value in consideration.
if the current number is not smaller than the pivot then we just advance the value pointer else we swap the value with
the border and advance both pointers, when the list ends, we are going to swap the pivot with the border value, we will see
that the value left of pivot will be smaller than the pivot and values to the right of pivot will be greater than the
pivot. 

After calling partition, we will see if there are elements to the left of the pivot or to the right of pivot and we will append
((l, pivot - 1)) and (pivot + 1, h) in either of the cases we will keep popping and append the stack till the stack is empty and we will
finally return the array
Time Complexity-Worst case is O(nsquared) since partition function will run n times and while loop in stack not empty can also run worst case n times
so Time complexity is O(nsquared)
Space Complexity- i have to analyse it
Issues- Space complexity and leetcode passing 11/13 test cases; i used Youtbe for learning this 
"""


# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivotindex = h
    border=l
    for i in range(l, h+1):
        if arr[i]<arr[pivotindex]:
            arr[i], arr[border]=arr[border], arr[i]
            border += 1
    arr[pivotindex], arr[border] = arr[border], arr[pivotindex]
    return border

  #write your code here

def quickSortIterative(arr, l, h):
    stack = deque()
    stack.append((l, h))
    while stack:

        l, h = stack.pop()
        pivot = partition(arr, l, h)

        if pivot - 1 > l:
            stack.append((l, pivot - 1))

        if pivot + 1 < h:
            stack.append((pivot + 1, h))


# arr=[5,1,1,2,0,0]
# arr=random.random(range(0,10),10)
# arr=random.sample(range(0,10),10)
arr=[0,0,0,0,1,1,2,1,0,0,0,3]
# arr=[1,2,4,5,6,0,8]
# arr = random.sample(range(0, 20), 20)
print("initial array is", arr)
n = len(arr)
print(quickSortIterative(arr, 0, n - 1))
print("Sorted array is:")
for i in range(n):
    print(arr[i])
