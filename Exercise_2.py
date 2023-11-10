'''
Time Complexity : O(n log n), where n is elements in array
Space Complexity : O(log n) Average case, Worst case O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
Your code here along with comments explaining your approach: choosing rightmost element as pivot.
'''

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    i = low #pointer for greater element

    for j in range(low, high):
        if arr[j]<=pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
    
    arr[i], arr[high] = arr[high], arr[i]
    return i

  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        pivotIndex = partition(arr, low, high)
        quickSort(arr, low, pivotIndex-1)
        quickSort(arr, pivotIndex+1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i], end=" "), 