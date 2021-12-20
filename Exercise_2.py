# Python program for implementation of Quicksort Sort
# Time Complexity: O(n^2) (worst case) Best Case: O(nlogn) (cannot be acheived)
# Space Complexity: O(log n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while i < len(arr) and arr[i] <= pivot:
            i+=1
        while arr[j] > pivot:
            j-=1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if (low < high):
        j = partition(arr, low, high)
        quickSort(arr, low, j)
        quickSort(arr, j+1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
