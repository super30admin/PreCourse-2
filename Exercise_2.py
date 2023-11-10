# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    # pivot is chosen at the last element

    pivot = arr[high]
    # greater element is initialized
    greater_element = low-1

    for j in range(low,high):
        if arr[j] <= pivot:
            # If the element is less than pivot swap it with greater element
            greater_element = greater_element + 1
            arr[greater_element],arr[j] = arr[j], arr[greater_element]

    # Swap the greater element and the pivot
    arr[greater_element+1],arr[high] = arr[high], arr[greater_element+1]
    # return the partitioning index
    return greater_element+1


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # Calling the partition method to find the pivot index
        index = partition(arr, low, high)
        # Calling quick sort for first half before pivot
        quickSort(arr, low, index -1)
        # Calling quick sort for second half after pivot
        quickSort(arr, index + 1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


