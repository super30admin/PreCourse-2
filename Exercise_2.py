# Python program for implementation of Quicksort Sort 
#time complexity: O(nlogn) - best case, O(n^2) - worst case
# Space complexity: O(logn) - best case , O(n) - for the recursion stack for worst case

# give you explanation for the approach
def partition(arr,low,high):

    slot = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[slot] = arr[slot], arr[j]
            slot += 1

    arr[slot], arr[high] = arr[high], arr[slot]
    return slot  

# Function to do Quick sort 
def quickSort(arr,low,high): 

    if low < high:
        pivot_indx = partition(arr, low, high)
        quickSort(arr, low, pivot_indx-1)
        quickSort(arr, pivot_indx+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
