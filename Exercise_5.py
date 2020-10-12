# Python program for implementation of Quicksort
"""
Time Complexity : O(nlogn)
Space Complexity : O(n)
Did this code successfully run on Leetcode : I don't know if this question is on Leetcode
                                            Please let me know in case it is
Any problem you faced while coding this : Yes, I havd some issues understanding quick sort
Your code here along with comments explaining your approach
"""
"""
The partition operation is the same as the earlier question.
For the other method, we are using a stack to keep the track of left and right positions of the subarrays 
for which we were using recursion earlier. Everything else is the same
"""
# This function is same in both iterative and recursive


def partition(arr, l, h):

    pos = l-1
    pvt = arr[h]
    for x in range(l, h):
        if arr[x] <= pvt:
            pos += 1
            arr[pos], arr[x] = arr[x], arr[pos]
    arr[pos+1], arr[h] = arr[h], arr[pos+1]
    return pos+1


def quickSortIterative(arr, l, h):
    length = h - l + 1
    temp = [0] * (length)
    top = 0
    temp[top] = l
    top += 1
    temp[top] = h
    while top >= 0:

        h = temp[top]
        top -= 1
        l = temp[top]
        top -= 1
        pivot = partition(arr, l, h)
        if pivot + 1 < h:
            top += 1
            temp[top] = pivot + 1
            top += 1
            temp[top] = h
        if pivot-1 > l:
            top += 1
            temp[top] = l
            top += 1
            temp[top] = pivot - 1
