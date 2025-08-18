# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Time Complexity :O(N^2)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
# Your code here along with comments explaining your approach: Select the rightmost element as the pivot. Rearrange the array so that elements smaller than the pivot are on the left, and elements greater than the pivot are on the right. Return the pivot’s index. Recursively apply the same process to the left and right sub-arrays created by the pivot.
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi -1)
        quickSort(arr, pi + 1, high)

    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
