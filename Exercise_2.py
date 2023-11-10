# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Take a random element and the elements lower than that go on the left partition
# elements greater in right partition
# pivot position is set first and then left part is sorted using the same process and right part is sorted using the same process
def partition(arr,low,high):
  
  
    #write your code here
   # Choose the rightmost element as pivot
    pivot = arr[high]
 
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])
 
    # Swap the pivot element with
    # the greater element specified by i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
 
    # Return the position from where partition is done
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
     if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high) 
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
