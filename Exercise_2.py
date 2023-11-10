#Time Complexity : O(nlogn)
 #Space Complexity : O(n)
 #Did this code successfully run on Leetcode :
 #Any problem you faced while coding this :
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot, ptr = arr[high], low
    for index in range(low, high):
        if arr[index] <= pivot:
            arr[index], arr[ptr] = arr[ptr], arr[index]
            ptr += 1
    arr[ptr], arr[high] = arr[high], arr[ptr]
    return ptr
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if len(arr) == 1: 
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)  
    return arr
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
