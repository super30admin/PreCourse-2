# Python program for implementation of Quicksort

# Time Complexity:
# - Average case: O(n log n)
# - Worst case: O(n^2) 
# Space Complexity: O(log n) 

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# Function to do Quick sort (iterative)
def quickSortIterative(arr, low, high):
    size = high - low + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        p = partition(arr, low, high)

        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        if p+1 < high:
            top = top + 1
            stack[top] = p+1
            top = top + 1
            stack[top] = high

# Driver code to test the above code
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
