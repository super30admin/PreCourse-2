# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = high
    i = low

    for j in range(low, high):
        if arr[j] <= arr[pivot]:
            arr[j], arr[i], = arr[i], arr[j]
            i += 1

    arr[pivot], arr[i] = arr[i], arr[pivot]

    return i

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, 0, pivot - 1)
        quickSort(arr, pivot + 1, high)


if __name__ == '__main__':
# Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr,0,n-1)
    print("Sorted array is:")
    print(arr)



