# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i <= j:
        #moving one pointer to right
        while arr[i] < pivot:
            i += 1
        #moving other pointer to left
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
    return i


# Function to do Quick sort
def quickSort(arr, low, high):
    print("BEFORE",arr)
    print(arr)

    if len(arr) == 1:
        return arr

    if low < high:

        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p,high)
    # write your code here


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" % arr[i]),
