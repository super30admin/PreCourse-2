# Time Complexity : O(n log n) on average, O(n^2) in the worst case
# Space Complexity : O(log n) due to the recursive stack
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort Sort
 
# give you explanation for the approach
def partition(arr,low,high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    i = low - 1  # index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1  # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap the pivot element with the element at i+1
    return i + 1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        # pi is partitioning index, arr[pi] is now at the right place
        pi = partition(arr, low, high)

        # Recursively sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
