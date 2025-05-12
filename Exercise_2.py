# Python program for implementation of Quicksort Sort 
# Author : Akaash Trivedi
# Time Complexity :
# Space Complexity :
# Did this code successfully run on Leetcode : Leetcode #912
# Any problem you faced while coding this : No
  
# give you explanation for the approach
def partition(arr,low,high):
    i = low
    j = high -1
    pivot = arr[high]

    while i < j:
        # look for element that is greater than pivot
        while i < high and arr[i] < pivot:
            i += 1
        # look for element smaller than pivot
        while j > low and arr[j] >=pivot:
            j -= 1
        
        # swap elements at i and j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # move pivot at correct position
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
  
    return i

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        partitionPosition = partition(arr, low, high)
        quickSort(arr, low, partitionPosition -1)
        quickSort(arr, partitionPosition + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])