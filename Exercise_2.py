# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    '''
    Considers pivot as last element (did not use temp
    variable for interchanging)
    This function places all elements less than pivot
    to its left and greater than pivot on its right
    '''
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
    # write your code here


# Function to do Quick sort
def quickSort(arr, low, high):
    '''
    Call quicksort function based on partition
    and call it recursively on left and right
    side of the array.
    Time Complexity: O(n^2)
    Space Complexity: O(log n)
    '''
    if low < high:
        part = partition(arr, low, high)

        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)
    # write your code here


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


