# Python program for implementation of Quicksort Sort 
# Time Complexity: O(nlog n)
# Space Complexity: O(n) in worst case

# We take a pivot, in this case the last element and have the partition , put all the elements less than it to one half and greater than it to another half. Then we subsequently perform the quick sort on those partittions.

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    while low < high:
        if arr[low] < pivot:
            i += 1
            arr[i], arr[low] = arr[low], arr[i]
        low += 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low > high:
        return
    
    par = partition(arr, low, high)
    quickSort(arr, low, par - 1)
    quickSort(arr, par + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
