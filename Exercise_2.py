# Python program for implementation of Quicksort Sort 
# Time Complexity : O(n logn)
# Space Complexity : O(logn)
# Did this code successfully run on Leetcode : Couldn't find on leetcode
# Any problem you faced while coding this : It was clear
  
# give you explanation for the approach
def partition(arr,low,high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)
  
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 