# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time Complexity : O(N log N) --> best and average case; O(n^2) --> worst case
# Space Complexity :O(log N) --> best and average case; O(n) --> worst case
# Did this code successfully run on Leetcode? : Verified by succesfully running on code editor
# Any problem you faced while coding this : No

def partition(arr,low,high):
  
  
    #write your code here
    i = low
    j = high-1
    pivot = arr[high]
    
    while i<j:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i 
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) == 1:
        return arr
    if low<high:
        x = partition(arr, low, high)
        quickSort(arr, low, x-1)
        quickSort(arr, x+1, high)
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
