"""Time Complexity : O(nlog(n))
Space Complexity : O(log(n))
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
"""
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #store pivot index and initialize pivot
    pivot_index = low
    pivot = arr[low]
    #run loop still low crosses high and when 
    # it happens we swap it with element on higher end
    while low < high:
        #while elements on low index are less than pivot
        #we increment low
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        #while elements on high index are high than pivot
        #we decrement high
        while arr[high] > pivot:
            high -= 1
        #whenever high and low indexes cross each other
        #we swap elements on high and low index with 
        # each other
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    #swap pivot with element on high index
    #which puts pivot on correct position
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return high

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        #p_index is the index to 
        #partition the array 
        p_index = partition(arr, low, high)
        #Sort elements before and after 
        # the partition index
        quickSort(arr, low, p_index - 1)
        quickSort(arr, p_index + 1, high)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
