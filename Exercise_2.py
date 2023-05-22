# Python program for implementation of Quicksort Sort
# Submitted by : Aryan Singh_RN12MAY2023
# Time Complexity : O(nlog n) on average, worst case : O(n^2)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Not applicable
# Any problem you faced while coding this : No 
  
# Selecting last element as pivot will give worst case time complexity of O(n^2) when array is already sorted
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
