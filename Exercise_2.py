# Python program for implementation of Quicksort Sort 
# give you explanation for the approach

# Given an array arr[], partition the array by assuming last element as pivot element.
# The partition of an array must satisfy the following two conditions:
# Elements smaller than the pivot element appear before pivot in the array.
# Elements larger than or equal to the pivot element appear after pivot it in the array.

# Time and Space complexity: 
# Time Complexity: O(n log n)
# Space Complexity: O(log n)
def partition(arr,low,high):
    #write your code here
    # Taking the last element as the pivot
    pivot = arr[high]
    i = low - 1 # Initial boundary before the first element ie 'low'
    
    for j in range(low, high):
        # Checking if the current element is smaller or equal to the pivot
        if arr[j] <= pivot:
            # Check the next value
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swapping the value using python unpacking
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # swapping the pivot value to the right position
    return i + 1


# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        # partition the array
        part = partition(arr, low, high)
        
        # recursive call
        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),
