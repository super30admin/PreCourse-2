# Time Complexity :  
# Average Case: O(n log n)  
# Worst Case: O(n^2) — occurs when the smallest or largest element is always picked as the pivot (e.g., sorted or reverse-sorted arrays)  
# Best Case: O(n log n) — when the pivot always splits the array into two nearly equal halves

# Space Complexity :  
# O(log n) for the recursive call stack in the average case  
# O(n) in the worst case due to deep recursion (unbalanced partitions)

# Did this code successfully run on Leetcode :  
# Yes, it works correctly. It matches the expected output for sorted arrays.

# Any problem you faced while coding this :  
# Understanding the pivot placement and maintaining index boundaries in the partition function can be tricky.  
# Using the last element as pivot may lead to worst-case performance on sorted inputs.  
# Also, Python has a recursion limit (~1000), which may cause RecursionError on very large arrays.

# Your code here along with comments explaining your approach:
def partition(arr, low, high):
       """
    This function implements the Lomuto partition scheme:
    - It selects the last element as pivot.
    - It places the pivot in its correct sorted position.
    - Elements smaller than or equal to the pivot are placed to its left.
    """

    pivot = arr[high]
    i = low - 1                    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
   
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
     """
    Main QuickSort recursive function.
    It recursively partitions the array around a pivot until the array is sorted.
    """
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)   # left side
        quickSort(arr, pi + 1, high)  # right side
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 


  
 
