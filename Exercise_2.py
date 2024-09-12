# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Select a pivot element, here last element is taken as the pivot element
# All the elements less than the pivot are arranged such that they are before the pivot in the array
# and all the elements greater than the pivot are placed after the pivot element in the array.
# and pivot is placed at its proper position
# Repeat above procedure for elements on either side of the pivot

def partition(arr,low,high):
  
  
    #write your code here
    low_index = (low - 1)
    pivot = arr[high]
    
    for i in range(low, high):
        if arr[i] <= pivot:
            low_index = low_index + 1
            arr[low_index], arr[i] = arr[i], arr[low_index]
    arr[low_index+1], arr[high] = arr[high], arr[low_index+1]
    return (low_index+1)
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) == 1:
        return arr
    if low < high:
        index = partition(arr, low, high)
        
        quickSort(arr, low, index - 1)
        quickSort(arr, index + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
