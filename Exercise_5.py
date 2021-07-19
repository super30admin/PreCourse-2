# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            # increment
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


def quickSortIterative(arr, l, h):
    # Creating stack
    size = h - l + 1
    stack = [0] * (size)

    top = -1
    # Pushing initial values
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
    # Popping from stack
    while top >= 0:
        # Pop
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        # Set index element at its correct position
        index = partition(arr, l, h)
        # For elements on the left
        if index - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = index - 1
        # For elements on the right
        if index + 1 < h:
            top = top + 1
            stack[top] = index + 1
            top = top + 1
            stack[top] = h

# Added driver code
arr = [99,12,5,16,121,83,0,53]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
   print(arr[i],end=" ")