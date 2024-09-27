# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
def partition(arr, low, high):
    small = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if (arr[j] <= pivot):
            small = small + 1
            arr[small], arr[j] = arr[j], arr[small]

    arr[small + 1], arr[high] = arr[high], arr[small + 1]

    return small + 1


def quickSort(arr, low, high):
    if (len(arr) == 1):
        return arr

    if (low < high):
        split_array = partition(arr, low, high)

        quickSort(arr, low, split_array - 1)
        quickSort(arr, split_array + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" % arr[i])
 
