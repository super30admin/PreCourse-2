# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Python program for implementation of Quicksort
from collections import deque

# This function is same in both iterative and recursive
def partition(arr, l, h):
  # assigning an last element from the list as pivot element
    pivotElement = arr[h]
    # assigned the greatest element
    value = (l-1)
    # checking each element from the list with the pivot
    for j in range(l, h):
        # checking if the element is <= pivot element, if satisfies swap it with larger element
        if arr[j] <= pivotElement:
            value += 1
            # swap the taken element with the element of index j
            temp = arr[j]
            arr[j] = arr[value]
            arr[value] = temp
    # swap the pivot element with the larger element specified by value
    temp = arr[h]
    arr[h] = arr[value+1]
    arr[value+1] = temp
    return (value+1)

def quickSortIterative(arr, l, h):
    #creating stack to store low and high index
    stack = deque() 
    #for the low and high values of the taken list
    l = 0 
    h = len(arr) - 1  
    #inserting low and high values 
    stack.append((l, h)) 
    #iterate until stack is empty
    while stack: 
        #pop the last inserted values and get low and high index values
        l, h = stack.pop() 
        #sort the elements with pivot value
        pivot = partition(arr, l, h) 
        #inserting the sublist values which are less than pivot value into the stack
        if pivot - 1 > l:
            stack.append((l, pivot - 1)) 
        #inserting the sublist values which are higher than pivot value into the stack
        if pivot + 1 < h:
            stack.append((pivot + 1, h))

# Driver code to test above
arr = [0, 3, 6, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])