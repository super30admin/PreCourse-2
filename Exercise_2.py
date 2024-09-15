#Time Complexity :  O(nlogn)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
       
    # Initializing pivot's index 
    piv_index = low
    pivot = arr[piv_index]
    
    while low < high:
         
        # Increment the low pointer till it finds an element greater than  pivot
        while low < len(arr) and arr[low] <= pivot:
            low += 1
             
        # Decrement the high pointer till it finds an element less than pivot
        while arr[high] > pivot:
            high -= 1
   
        # swap the numbers on start and end if low and high not crossed each other
        if(low < high):
            arr[low], arr[high] = arr[high], arr[low]
     
    # Swap pivot element with element on high pointer
    arr[high], arr[piv_index] = arr[piv_index], arr[high]
    
    # Returning high when divided arr in two parts
    return high
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
  if (low < high):
         
        # p is partitioning index
        p = partition(arr,low, high)
         
        # Sort elements before partition and after partition
        quickSort(arr,low, p - 1)
        quickSort(arr,p + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),