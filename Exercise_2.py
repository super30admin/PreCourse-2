# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time Complexity : O(n^2)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No


def partition(arr,low,high):
  
  
    #write your code here
    i = low - 1
    pivot = arr[high]
  
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

  

# Function to do Quick sort 
def quickSort(arr,low,high):

    
    #write your code here
    if low < high:
        j = partition(arr, low, high)
        quickSort(arr, low, j-1)
        quickSort(arr, j+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
