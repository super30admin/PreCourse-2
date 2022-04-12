# Python program for implementation of Quicksort Sort 
# Time Complexity : Average: O(Nlog(N)) worst: O(N^2)
# Space Complexity : O(log(N))

# give you explanation for the approach
def partition(arr, low, high):
    pivot = arr[int((low+high)/2)] # middle element is taken as pivot
    # swap elements to left and right of pivot that are out of order
    while low <= high:
        while arr[low] < pivot: 
            low += 1
        while arr[high] > pivot:
            high -= 1
        
        if low <= high: # low and high is not crossed
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    # low will be the pivot index
    return low  
  

# Function to do Quick sort 
def quickSort(arr, low, high): 
  if low < high:
      partition_index = partition(arr, low, high)
      quickSort(arr, low, partition_index-1)
      quickSort(arr, partition_index+1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
