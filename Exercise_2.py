# Python program for implementation of Quicksort Sort 
# Time Complexity : O(n^2)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# give you explanation for the approach
def swap(i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    return arr

def partition(arr,low,high):
    i, j = low, high
    pivot = low
    while i < j:
        while arr[i] < arr[pivot]:
            i += 1
        while arr[j] > arr[pivot]:
            j -= 1
        if i < j:
            arr = swap(i, j)
    arr = swap(pivot, j)

    return j
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        j = partition(arr, low, high)
        quickSort(arr, low, j-1)
        quickSort(arr, j+1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
