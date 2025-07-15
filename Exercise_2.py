# Python program for implementation of Quicksort 
# Time Complexity: O(n log n)
# Space Complexity: O(log n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : I had to revisit the quicksort algorithm concepts. It took me some time to recall and implement the correct approach.

def partition(arr,low,high):
    pivot = arr[high] # Choosing last element as pivot
    i = low-1
    for j in range(low,high): # Traverse through all elements, compare each with pivot
        if arr[j]<=pivot:
            i+=1    # If element smaller than pivot is found, swap it
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return i+1 # Return the partition index
    
 
def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1) 
        quickSort(arr,pi+1,high)
        
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
