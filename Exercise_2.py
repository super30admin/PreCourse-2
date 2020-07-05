# Python program for implementation of Quicksort Sort

# give you explanation for the approach

# we first partition the array with the help of helper function partition
#  in two and then make recurcive calls to sort the array by calling quickSort between arr{low, pivot} and arr{pivot, high}
def partition(arr,low,high):
    i = ( low-1 )
    pivot = high
    for j in range(low , high):
        if arr[j] < arr[pivot]:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
    #write your code here


# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

    #write your code here

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
