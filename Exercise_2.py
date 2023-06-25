# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

#time complexity O(n log n)
#space complexity O(log n) 
def partition(arr,low,high):
  
  i = low - 1  # Index of smaller element
  pivot = arr[high]  # Pivot element

  for j in range(low, high):
        #current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i = i + 1  
            arr[i], arr[j] = arr[j], arr[i]  

  arr[i + 1], arr[high] = arr[high], arr[i + 1]  
  return i + 1 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low < high:
       
        partition_index = partition(arr, low, high)

        # Recursive call on the subarrays
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
