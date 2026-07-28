# Time Complexity:
# Average Case: O(n log n)
# Worst Case: O(n^2)

# Space Complexity:
# Average Case: O(log n)
# Worst Case: O(n)

# Did this code successfully run on LeetCode: Not directly applicable because LeetCode uses a different function format

# Any problem you faced while coding this: The main challenge was placing the pivot in its correct position and using the correct recursive boundaries

# Approach:
# 1. Select the final element as the pivot
# 2. Move all elements smaller than or equal to the pivot to its left
# 3. Move all elements greater than the pivot to its right
# 4. Return the pivot's final index
# 5. Recursively sort the left and right parts of the array


def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
