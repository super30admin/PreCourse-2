# Time Complexity: O(n log n) 
# Space Complexity: O(log n) due to the recursion stack 
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this :choosing the the right pivot and handling edge case for duplicate element in the array

def partition(arr,low,high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        # If the current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment the index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Swap pivot element with i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partitioning index

def quickSort(arr, low, high):
    if low < high:
        # Partition the array and get the partition index
        pi = partition(arr, low, high)
        # Recursively sort elements before and after the partition
        quickSort(arr, low, pi - 1)  # Left subarray
        quickSort(arr, pi + 1, high)  # Right subarray

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
