# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    #write your code here
    pivot = high
    pivot_index = low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i],arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return pivot_index

def quickSortIterative(arr, l, h):
    #write your code here
    if l>=h:
        return

    stack = [(l,h)]
    while stack:
        start, end = stack.pop(0)
        p = partition(arr, start, end)
        if p-1 > start:
            stack.append((start, p-1))
        if p+1 < end:
            stack.append((p+1, end))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" "),

"""
n = number of elements in the array
Space Complexity: O(log n) for the stack

Time Complexity:
O(n log n)
"""