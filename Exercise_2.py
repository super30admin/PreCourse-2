# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    # Did this code successfully run on Leetcode : yes
    # Any problem you faced while coding this : initially had i = -1 but this is recursively called, that was an error
    # Your code here along with comments explaining your approach
    #aim of partition is to put pivot in correct position, less elements on left, higher on right 
    #maintain larger element set when smaller element is encountered, swap with 1st largest

    #write your code here
    pivot_index = high
    i = low-1
    for j in range(low, pivot_index):
        if(arr[j]>arr[pivot_index]):
            continue
        else:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[pivot_index] = arr[pivot_index], arr[i+1]
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    # Time Complexity : O(n log n)
    # Space Complexity : O(log n) for the call stack I guess 

    #write your code here
    if(low<high):
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
