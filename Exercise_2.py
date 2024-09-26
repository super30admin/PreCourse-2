# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Function to do Quick sort 
"""
Time - O(n^2)
Space - O(1)
Idea - We divide the list according to partition and then sort the left and right list of the partition
"""
def quickSort(arr,low,high): 
    divide(arr, low, high)


def divide(arr, lo, hi):  
    if lo >= hi:
        return
    
    pivot = partition(arr, lo, hi)

    quickSort(arr, lo, pivot-1)
    quickSort(arr, pivot+1, hi)


def partition(arr,low,high):
    pivot = arr[low]
    swap_index = low + 1

    for i in range(low+1, high+1):
        if arr[i] < pivot:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swap_index += 1
    
    arr[low], arr[swap_index-1] = arr[swap_index-1], arr[low]
    return swap_index-1
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print(arr[i])
 
