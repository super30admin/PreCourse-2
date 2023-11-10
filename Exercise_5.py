# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    for j in range(l + 1, h + 1):
        if arr[j] < pivot:
            (arr[j], arr[i]) = (arr[i], arr[j])
            i += 1
    (arr[l], arr[i - 1]) = (arr[i - 1], arr[l])
    return i - 1

def quickSortIterative(arr, l, h):
    size = len(arr)
    stack = [0]*size
    index = 0
    stack[index] = l
    index += 1
    stack[index] = h

    while index >= 0:
        end = stack[index]
        index -= 1
        start = stack[index]
        index -= 1
        p = partition(arr, start, end)
        if p-1 > start:
            index += 1
            stack[index] = start
            index += 1
            stack[index] = p - 1
        if p+1 < end:
            index += 1
            stack[index] = p + 1
            index += 1
            stack[index] = end

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print(f"Sorted array is: {arr}")
