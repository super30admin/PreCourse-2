# Python program for implementation of Quicksort
# Time Complexity: O(N log N)
# Space complexity: O(n)
# This function is same in both iterative and recursive
def partition(arr,low,high): # Main logic which sorts the smaller elements to the left side and larger elements to the right side
    pivot = high
    p1 = low
    i = low-1 # Index to return at the end which is going to be at the correct position
    while p1 <= high:
        if arr[p1] < arr[pivot]:
            i += 1
            temp = arr[p1]
            arr[p1] = arr[i]
            arr[i] = temp
        p1 += 1
    temp = arr[high]
    arr[high] = arr[i+1]
    arr[i+1] = temp
    return i+1
def quickSortIterative(arr, low, high):

    length = high - low + 1
    stack = [0] * length # To emulate the recursion stack from recursive quicksort

    top = -1

    stack[top+1] = low
    stack[top+2] = high
    top += 2
    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        index = partition(arr, low, high)
        if index - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = index - 1

        if index + 1 < high:
            top += 1
            stack[top] = index + 1
            top += 1
            stack[top] = high


# Driver code to test above
arr = [10, 7, 8, 9, 20, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])


