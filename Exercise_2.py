# Python program for implementation of Quicksort Sort 
# Time Complexity : O(nlogn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Some implementation issues.
# give you explanation for the approach

def partition(arr,l, h):
    #write your code here
    #Selects the pivot and two pointers
    pivot = arr[l]
    i = l
    j = h
    
    #Compares the pivot with other numbers 
    while (i < j):
        while (arr[i] <= pivot and i <= h - 1):
            i += 1
        while (arr[j] > pivot and j >= l + 1):
            j -= 1
        
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
     #Once done, swap the pivot with j to it's position  
    arr[l], arr[j] = arr[j], arr[l]
    return j

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    
    if (low < high):
        #partition the array 
        pIndex = partition(arr, low, high)
        
        #calls the smaller side of pivot for sorting
        quickSort(arr, low, pIndex - 1)

        #calls the larger side of pivot for sorting
        quickSort(arr, pIndex + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 

 
