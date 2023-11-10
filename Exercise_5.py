# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    # write your code here
    i = low - 1
    x = arr[high]

    for j in range(low, high):
        if arr[j] <= x:

            # Increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quickSortIterative(arr, low, high):
    # write your code here

    
    size = high - low + 1
    stack = [0] * size

    
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


        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

       

        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high


# Driver code to test above
arr = [4, 3, 5, 2, 1, 3, 2, 3, 6, 3, 5, 6]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])