# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    # choose right most element as pivot
    pivot = arr[high]
    # pointer for greater element 
    i = low - 1
    # loop through array
    for j in range(low, high):
        if arr[j] <= pivot:
            # if the element at j pointer smaller than pivot then swap element i and j position
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    # swap the pivot element with the element at i+1 position
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    # return partition position
    return i+1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if (low < high):
        # find the pivot element for the arr
        pivot = partition(arr, low, high)
        # recursive call for left side of the array
        quickSort(arr, low, pivot - 1)
        # recursive call for right side of the array
        quickSort(arr, pivot + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
