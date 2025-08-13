# Python program for implementation of Quicksort Sort 
"""
Time Complexity: O(n2) worst
Space Complexity: O(n) worst
"""
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[low] #pivot is first element
    i = low
    
    for j in range(low+1, high+1):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
            
    arr[i], arr[low] = arr[low], arr[i]
    return i
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    # if pivot is suppoed to be median, swap the chosen element into low, run the same partition_first() where pivot = arr[low], and you’ve upgraded Quick Sort’s robustness without rewriting the whole algorithm.
    # In the partition function, the pivot will be taken as the first eleemtn.,
    if low<high:
        
        pivot = partition(arr, low, high)
        
        quickSort(arr, pivot + 1, high)  
            
        quickSort(arr, low, pivot - 1) 
    return arr 
     
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
