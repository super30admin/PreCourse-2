# Python program for implementation of Quicksort Sort 

# Approach Explanation:
# QuickSort is a divide-and-conquer algorithm that works by:
# 1. Selecting a 'pivot' element from the array
# 2. Partitioning the array around the pivot (elements smaller than pivot go to the left, larger to the right)
# 3. Recursively applying the above steps to the sub-arrays

# Time Complexity:
# - Best Case: O(n log n) - When the pivot divides the array into roughly equal halves
# - Average Case: O(n log n) - Across all possible inputs
# - Worst Case: O(n²) - When the smallest or largest element is always chosen as pivot (e.g., already sorted array)
#
# Space Complexity:
# - O(log n) - For the recursion stack in the average case
# - O(n) - In the worst case when the recursion is unbalanced

def partition(arr,low,high):
    # Choose the rightmost element as pivot
    pivot = arr[high]

    # Index of smaller element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot at its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the partition index
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at the right place
        pi = partition(arr, low, high)
        
        # Separately sort elements before and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
  
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
