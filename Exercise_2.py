# Time Complexity : Average O(n log n), Worst O(n^2) if pivot choices are poor
# Space Complexity : O(log n) due to recursion stack (in-place sort)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Approach:
# 1. Choose a pivot (here we choose the last element in the current subarray).
# 2. Partition the array into two halves:
#    - All elements <= pivot move to the left side.
#    - All elements > pivot move to the right side.
#    This is done using a pointer `i` to track the position where the next smaller element should go.
# 3. Swap the pivot into its correct sorted position.
# 4. Recursively apply the same logic to the left and right subarrays (excluding the pivot).
# 5. Sorting happens in-place, requiring no extra array.

# Python program for implementation of Quicksort Sort
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]  # choosing last element as pivot
    i = low - 1  # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # place pivot in correct position
    return i + 1

  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
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
  
 
