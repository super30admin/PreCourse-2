# Python program for implementation of Quicksort Sort 
# Time complexity:  O(nlog n) - best case
#                   O(n^2) - worst case

   
# give you explanation for the approach
# 
def partition(arr,low,high):
    # write your code here
    # assign first element of array as pivot
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # traverce array from left to right 
        # increase i until you find element greater than pivot
        while arr[i] <= pivot and i < high:
            i += 1

        # traverce array from right to left 
        # decrease j until you find element greater than pivot   
        while arr[j] > pivot and j >= low:
            j -= 1
        
        # If i and j did not cross then swap elements 
        if i < j:
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    # If i and j crossed each other we found sorted position for pivot
    # swap pivot with partitioning location 
    (arr[low], arr[j]) = (arr[j], arr[low])

    # retun partitioning position
    return j

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
  
    # If there are atleast two elements
    if low < high:
       
       # j is the position where partition is done
       j = partition(arr, low, high)
       
       # left side of pivot
       quickSort(arr, low, j)
       
       # right side of pivot
       quickSort(arr, j+1, high)

    # Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
