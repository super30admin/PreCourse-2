# Time Complexity : O(N log N) We divide the array into log N partitions for sorting, worst case for sorted array O(N^2)
# Space Complexity : O(log N) Sorted in-place, the log N memory is used for the recurssive call stack

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # Chosing pivot as rightmost element
    pivot = arr[high]
    
    left, right = low, high -1
    while left <= right:
        while arr[left] <pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        # Found left an right indices that need to be swaped
        if left < right: # swap only if left is still smaller than right
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
        else:
            # Swap pivot with the left pointer as its the correct index     
            temp = arr[left]
            arr[left] = arr[high]
            arr[high] = temp
 
    return left

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        # Get the partition index and recursively sort
        partition_index = partition(arr, low, high)
        
        quickSort(arr, low, partition_index-1)
        quickSort(arr, partition_index+1, high)
  
# Driver code to test above 
arr = [4,3,2,1]  
quickSort(arr,0,len(arr)-1) 
print ("Sorted array is:") 
print(arr)
arr2 = [10,7,8,9,1,5]
quickSort(arr2,0,len(arr2)-1)
print(arr2)
arr2 = [1,2,3,4,5,6,7]
quickSort(arr2,0,len(arr2)-1)
print(arr2)

  
 
