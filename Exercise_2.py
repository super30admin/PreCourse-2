# Python program for implementation of Quicksort Sort 
 # // Time Complexity : O(nlog n)
# // Space Complexity : O(log n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : 
# give you explanation for the approach
def partition(arr,low,high):

    i = low -1
    pivot = arr[high] 

    for j in range(low , high):
        if arr[j] <= pivot:
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:
        return arr
    
    if len(arr) == 0:
        return None
    
    if low <= high:

        partition_index = partition(arr,low,high)

        quickSort(arr, low, partition_index-1)
        quickSort(arr,partition_index + 1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(arr) 
  
 
