# Python program for implementation of Quicksort Sort 
  
# give your explanation for the approach

# Time Complexity : Best case time complexity is O(nlogn) for Quick Sort when the subarrays created after the partition are almost equal in size. But the worst case time complexity is O(n^2) when the partition function constantly returns unbalanced subarrays.
# Space Complexity : Best case space complexity is O(logn) for perfectly balanced recursion algorithm. But for an unbalanced recursion, the time complexity will be O(n)
# Did this code successfully run on Leetcode : Yes, but the code didn't allow for worst case scenario for time complexity. So the implementation there was slightly different, using Stacks to keep track of the subarrays to avoid recursion code calls.
# Any problem you faced while coding this : No

# The partition function is used to divide an array using the pivot. The elements with higher value are placed to the right of the pivot and the elements with the lower value to the left
def partition(arr,low,high):
    #write your code here
    # A pivot is an element around which the Quick sorting of an array occurs. It can be any element, but the choice of the element affects the efficiency of the algorithm. Here, I have chosen the last element of the array as the pivot.
    pivot = arr[high]
    i = low - 1 # i maintains the pivot index. To calculate the correct index, i is kept as an index outside of the chosen array/subarray range
    for j in range(low, high): # Iterate through the array
        if arr[j] <= pivot: # If the current element is smaller than the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap the current element with the element at index i
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Swap the pivot element with the next element to get the pivot at the correct position
    return i + 1 # Return the pivot element current index
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if len(arr) == 0:
        print("Empty array")
        return
    elif len(arr) == 1:
        print("Only one element in array")
        return
    elif low < high:
        pivotIndx = partition(arr, low, high) # Identify the index of the pivot element using the partition function
        quickSort(arr, low, pivotIndx - 1) # Quick sort the left half (elements smaller than the initially chosen pivot)
        quickSort(arr, pivotIndx + 1, high) # Quick sort the right half (elements larger than the initially chose pivot)
  
# Driver code to test above 
arr = [10, 34, 99, 9, -1, -2, 7, 8, 9, 1, 5] 
n = len(arr)
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
