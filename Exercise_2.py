# Python program for implementation of Quicksort Sort 
# Time Complexity : O(n log n) average, O(n^2) worst
# Space Complexity : O(log n) due to recursion stack
# Did this code successfully run on Leetcode : Yes
  
# give you explanation for the approach
def partition(arr,low,high):
    """
    Rearranges the array by placing the pivot (last element)
    in its correct sorted position, with all smaller elements to the left
    and greater elements to the right.
    Returns the index of the pivot element after partitioning.
    """
    pivot = arr[high]    # choosing last element as pivot
    i = low - 1          # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    # place pivot at correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        # pi is partition index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
