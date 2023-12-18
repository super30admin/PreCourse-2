# Python program for implementation of Quicksort Sort 
# // Time Complexity : O(NLOGN)
# // Space Complexity : O(n) since we are using an array to store elements
# // Did this code successfully run on Leetcode : NA
# // Any problem you faced while coding this : None
def partition(arr,low,high):
  
    #write your code here
    pivot = (low+high)//2
    lesserThanPivot = low

    while low<=high:
        if arr[low] < arr[pivot]:
            arr[lesserThanPivot],arr[low] = arr[low],arr[lesserThanPivot]
            if lesserThanPivot == pivot:
                pivot = low
            lesserThanPivot += 1
        low += 1
        
    
    arr[lesserThanPivot],arr[pivot] = arr[pivot],arr[lesserThanPivot]

    return lesserThanPivot
        
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low >= high:
        return

    #write your code here
    pivotIndex = partition(arr,low,high)

    quickSort(arr,low,pivotIndex-1)
    quickSort(arr,pivotIndex+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 

n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
  
 
