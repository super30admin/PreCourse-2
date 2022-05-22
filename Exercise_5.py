# Time Complexity : O(n*n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# iterative way
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


# sort
def quick_sort(arr, l, h):
    # Creation of a stack
    size = h - l + 1
    stack = [0] * (size)
    # initialization
    top = -1
    # push initial values
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    # pop from stack
    while top >= 0:
        # Pop
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        # Set pivot element at its correct position
        p = partition(arr, l, h)
        # elements on the left
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        # elements on the right
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# main
arr = [2, 5, 3, 8, 6, 5, 4, 7]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:")
print(arr)

