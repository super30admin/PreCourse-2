# Python program for implementation of Quicksort Sort

# Time Complexity - O(nlogn) - Each iteration we divide the array by the pivot
# hence O(logn) and we traverse through the array to swap the elements
# lesser than pivot hence O(n).
# Space complexity - O(n) - Stack space as we perform recursive calls.

# Taking element at last position(high) as pivot. Now traversing through the arr and
# swap all elements lesser than pivot to the pointer 'p'. Once traversing complete array
# is done, we swap pivot element with position 'p'. This makes all the elements before p
# lesser than pivot and all elements after p as greater than pivot. Now we need to sort the
# elements before and after pivot.
def partition(arr, low, high):
    pivot = arr[high]
    p = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[p], arr[i] = arr[i], arr[p]
            p += 1
    arr[p], arr[high] = arr[high], arr[p]
    return p


# Function to do Quick sort
# We keep dividing the array by the pivot and sorting the array before
# and after pivot using quick sort.
def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)



# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


