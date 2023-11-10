# Python program for implementation of Quicksort Sort 
  


# give you explanation for the approach
"""
We take a pivot in array then we shift all elements lower that the pivot to the left and the higher elements to the right
we do this recursively, by breaking down into smaller sub arrays 

Time complexity : avg O(n * logn) worst O(n*n)
Space Complexity : normal O(1) 
"""
def partition(arr, low, high):
    pivot = arr[high]
    l = low -1
    
    for i in range(low, high):
        if arr[i] <= pivot:
            l = l+1
            arr[l], arr[i] = arr[i], arr[l] # swap 
    arr[l + 1], arr[high] = arr[high], arr[l+1]
    return l+ 1 
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr, low, high): 
    
    #write your code here
    if len(arr)<=1 :
        return arr
    if low < high:
        parti = partition(arr, low, high)
        quickSort(arr, low, parti - 1)
        quickSort(arr, parti +1 , high)  
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
