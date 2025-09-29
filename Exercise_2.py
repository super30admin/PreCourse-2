# Python program for implementation of Quicksort Sort 

# Time Complexity : O(n log n) 
# Space Complexity : O(log n) due to recursion stack
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : NA

def partition(arr, low, high):
    """
    This function takes the last element as pivot, 
    places the pivot at its correct position in sorted array,
    and puts smaller elements before it and larger after it.
    """
    i = low - 1  # index of smaller element
    pivot = arr[high]  # choose the last element as pivot

    # go through all elements and swap if smaller than pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    # put pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    """
    Main Quick Sort function that recursively sorts elements before and after partition
    """
    if low < high:
        # partition the array and get pivot index
        pi = partition(arr, low, high)

        # recursively sort the left part
        quickSort(arr, low, pi - 1)

        # recursively sort the right part
        quickSort(arr, pi + 1, high)
   
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
