#Time Complexity : worst case - O(n^2), on average - O(n log n)
#Space Complexity : O(log n)

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    l = low-1
    for i in range(low, high):
        if arr[i] < pivot:
            l = l+1
            arr[l], arr[i] = arr[i], arr[l]
    arr[high], arr[l+1] = arr[l+1], arr[high]
    return l+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        r = partition(arr, low, high)
        quickSort(arr, low, r-1)
        quickSort(arr, r+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
