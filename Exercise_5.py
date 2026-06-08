# Time Complexity : O(n log n) average, O(n^2) worst case: depends on pivot choice
# Space Complexity : O(n), explicit stack used to store subarray boundaries
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Approach: pick last element as pivot, place it in correct position via partition,
# then use an explicit stack to iteratively sort left and right subarrays

def partition(arr, l, h):
    pivot = arr[h]                             # last element is the pivot
    i = l - 1                                  # boundary of smaller elements

    for j in range(l, h):                      # scan every element except pivot
        if arr[j] <= pivot:                    # if element belongs on left side
            i += 1                             # expand left boundary
            arr[i], arr[j] = arr[j], arr[i]   # swap into left side

    arr[i+1], arr[h] = arr[h], arr[i+1]       # place pivot in correct spot
    return i + 1                               # return pivot's final index

def quickSortIterative(arr, l, h):
    stack = [0] * (h - l + 1)      # stack to store subarray boundaries
    top = -1                        # top = -1 means stack is empty

    top += 1
    stack[top] = l                  # push starting left index
    top += 1
    stack[top] = h                  # push starting right index

    while top >= 0:                 # loop until stack is empty
        h = stack[top]              # pop right boundary
        top -= 1
        l = stack[top]              # pop left boundary
        top -= 1

        p = partition(arr, l, h)    # partition array, p is pivot's final index

        if p - 1 > l:               # left subarray has more than 1 element
            top += 1
            stack[top] = l          # push left boundary
            top += 1
            stack[top] = p - 1      # push right boundary of left subarray

        if p + 1 < h:               # right subarray has more than 1 element
            top += 1
            stack[top] = p + 1      # push left boundary of right subarray
            top += 1
            stack[top] = h          # push right boundary

# Driver code
arr = [10, 80, 30, 90, 40, 50, 70]
n = len(arr)
print("Given array is")
print(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is")
print(arr)
