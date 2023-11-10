# Python program for implementation of Quicksort Sort
# Time Complexity - O(n*log(n)) for best and average cases.
#                   O(n^2) for worst case when the given array is already sorted.
  
# give you explanation for the approach
# below used partition is Hoare's partition.
# in this partition first element is picked as the pivot and two pointers are defines low and high
# low starts from 0 and traverses through the list until it finds the element > than pivot element
# then end starts from end of the array and traverses through the list until it finds the element < pivot element
# once we have elements > and < pivot, we swap those elements if low < end
# else if low > end we swap the element at pivot position with the element at end position and return the end position
# Now the element at pivot position is at its correct sorted position in the array and its index is called as pi(partition index)
# pi divides the array into 2 unsorted arrays to its left and right
# now simply apply quicksort to the elements left to pi and then to the right of pi

def partition(arr, low, high):
    pivot_index = low
    pivot = arr[low]
    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return high
  

# Function to do Quick sort 
def quickSort(arr, low, high):
    # no need to do partition if low >= high
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print(arr[i], end=" ")
  
 
