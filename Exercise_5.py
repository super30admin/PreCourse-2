# Python program for implementation of Quicksort

# Time Complexity : O(n)
# Space Complexity : O(1)
# Any problem you faced while coding this : No
# The code finds the element between low and high that is larger than pivot and swaps them
# This function is same in both iterative and recursive
def partition(arr, l, h):
    index = (l - 1)
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] <= pivot:
            index += 1
            arr[index], arr[j] = arr[j], arr[index]
    arr[index+1], arr[h] = arr[h], arr[index+1]
    return (index + 1)

# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Any problem you faced while coding this : No
# This is the iterative quicksort algorithm. We maintain a stack with the same size as the array
# We push in values larger than the pivot from the right array and smaller than the pivot from the left array and pop until empty
def quickSortIterative(arr, l, h):
    size = (h - l) + 1
    # Create a stack of size array
    stack = [0] * size

    top = 0
    stack[top] = l
    top += 1
    stack[top] = h

    # While stack is not empty
    while top > 0:
        h = stack[top]
        top -= 1
        l = stack[top]

        pivot = partition(arr, l, h)

        if pivot - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = pivot - 1

        if pivot + 1 < h:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = h

# Driver code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
