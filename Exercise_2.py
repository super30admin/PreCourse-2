#  Time Complexity : Average case: O(nlog(n)) Worst Case: O(n^2) 
#  Space Complexity : O(n) Size of the stack in recursion.
#  Did this code successfully run on Leetcode : Yes
#  Any problem you faced while coding this : No
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while(i<j):
        # increment i until arr[i] > pivot
        while(arr[i] <= pivot and i< high): 
            i += 1
        # decrement j until arr[i] <= pivot
        while(arr[j] > pivot and j> low):
            j -= 1
        
        # swap i and j position elements if i and j have crossed.
        if (i<j):
            arr[i],arr[j] = arr[j],arr[i]
        
        # repeat till i becomes greater than j
    # swap pivot and element at j.
    arr[low],arr[j] = arr[j],arr[low]
    return j  # return position which has been fixed.

# Function to do Quick sort 
def quickSort(arr,low,high):
    if(low<high):
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
    print ("%d" %arr[i])
