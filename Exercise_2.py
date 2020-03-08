# Python program for implementation of Quicksort Sort
"""
// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None
// Your code here along with comments explaining your approach
Algorithm explanation

Partition
- Choose pivot as last element
- Initialize left = 0
- for i =low to high+1
    - If arr[i] < pivot then swap arr[i] and arr[left]
    - left:=left+1
- Swap arr[left] and arr[pivot]

QuickSort
- If low <= high:
    a)Get the partition
    b)Sort the left half of partition index
    c)Sort the right half of partition index
"""
# give you explanation for the approach
def partition(arr,low,high):
    pivot = high
    left = low
    for i in range(low,high+1):
        if arr[i] < arr[pivot]:
            arr[i],arr[left] = arr[left], arr[i]
            left+=1

    arr[left],arr[pivot] = arr[pivot],arr[left]
    return left

  

# Function to do Quick sort 
def quickSort(arr,low,high):
    """
    Partition the array two halves and fix the pivot element in each case
    """
    if low < high:
        pivot = partition(arr,low,high)
        quickSort(arr,low,pivot - 1)
        quickSort(arr,pivot+1,high)

    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
arr = [10, 30, 20, 15, 23, 12]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  