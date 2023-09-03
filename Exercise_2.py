# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    pivot = arr[low]            # consider first element of the arr as pivot
    i = low + 1                 
    j = high
    while i <= j:              
        while i <= j and arr[i] <= pivot:   
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]         # swaping i , j
    arr[low], arr[j] = arr[j], arr[low]             # place the pivot at correct
    return j


# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here
    if low < high:
        pivot = partition(arr, low, high)       
        quickSort(arr, low, pivot - 1)          #for recursively sorting right part of the arr
        quickSort(arr, pivot + 1, high)         #for recursively sorting left part of the arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
