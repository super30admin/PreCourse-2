# Time Complexity : O(nlogn)
# Space Complexity : O(logn) for the recursive stack, no additional space due to in-place quick sort
# Did this code successfully run on Leetcode : Yes, but TLEd on large array consisting of just one number duplicated everywhere.
# Any problem you faced while coding this : -

# The quickSort function is called recursively for log(n) time and each time partitioning function 
# finds a pivot (last element is used in this) and then swaps O(n) elements. Hence leading to a time of O(nlogn).

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pidx = high
    i = low
    for j in range(low, high):
        if arr[j] < arr[pidx]:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[pidx] = arr[pidx], arr[i]
    return i

  
# Function to do Quick sort 
def quickSort(arr,low,high):
    if high-low+1 <= 1:
        return
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot-1)
    quickSort(arr, pivot+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
