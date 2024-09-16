# Python program for implementation of Quicksort Sort 

# give you explanation for the approach

# The first element of the interval is treated as the pivot
# The goal is to place the pivot in its sorted position
# That is, all elements to the left of the pivot are smaller and those to the right are greater

def partition(arr, low, high):
    # write your code here

    pivot = arr[low]
    i, j = low, high

    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if j >= low:
        arr[low], arr[j] = arr[j], arr[low]
        return j

    return low


# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here
    if low < high:
        j = partition(arr, low, high)
        quickSort(arr, low, j - 1)
        quickSort(arr, j + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
