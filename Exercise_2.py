# Python program for implementation of Quicksort Sort 


# Time Complexity : O(nlogn)- average, best and O(n^2) - worst case (like desecding and pivot is last element )
# Space Complexity :O(logn) - recursive stack 
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :
# in python (low,high) means low <=j < high
# swap method also new 
  

# give you explanation for the approach
# take two indices i,j i starts from low-1 and j starts from low 
    # now j runs from low to high-1 and i only moves forward if arr[j]<=pivot
    # after i moving forward we swap arr[i] and arr[j] till j reaches high -1 
    # atleast we swap arr[i+1] with pivot beacause till i it is less than pivot 
    # from i+1 it is greater so swap i+1 an dpivot , and pivot position is i+ 1

def partition(arr,low,high):
    pivot = arr[high]
    i = low -1
    for j in range (low, high):  # in python (low,high) means low <=j < high
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] # swapping function in python
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
  
    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        # low = high only one element sorted
        # low > high invalid or empty subarray nothing to sort
        pivot = arr[high]
        piv_index = partition(arr, low, high)
        quickSort(arr, low, piv_index - 1) # sorting left sub array
        quickSort(arr, piv_index + 1, high) # sorting right sub array

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
