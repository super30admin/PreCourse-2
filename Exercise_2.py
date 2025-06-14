"""
# Time Complexity : O(nlog N), best and average cases, 
# O(n^2) worst case if array is skewed with pivot at one end already sorted

# Space Complexity : O(logN) for recursive call stack on average, O(N) worse case

# Did this code successfully run on Leetcode : N/A, performed local testing

# Any problem you faced while coding this : 
> misremembered logic, was trying to pick pivot inside of quickSort method instead of partition method
> tried to perform partition logic with extra space instead of in-place
> missed writing base case for recursion

"""

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
import random


def partition(arr,low,high):
    pivot = high #picked as per Lomuto Partition - so that we can exclude from the window naturally
    pivotElement = arr[pivot]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivotElement:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    #now swap the pivot element with the last element
    arr[pivot], arr[i + 1] = arr[i + 1], arr[pivot]
    return i + 1
    


  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low >= high:
        return
    pivotIndex = partition(arr, low, high)
    quickSort(arr,low, pivotIndex - 1)
    quickSort(arr,pivotIndex + 1, high)

    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
