# Python program for implementation of Quicksort Sort 
# // Time Complexity : O(nlogn)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :
# yes used while loop in quicksort function instead of if.

# // Your code here along with comments explaining your approach
# quickSort - calls partition to get the pivot element and recursively calls itself to divide the array based on pivot
# Partition - fixes the first element as pivot, compares rest of the elements with pivot, swaps with lower elements with i,
# finally swaps the i-1 element with pivot element to place it in its position and returns the pivot element which is found at index i-1
  
# give you explanation for the approach
def partition(arr,low,high):
  
    pivot = arr[low]
    i = low + 1
    for j in range(low+1, high+1):
    
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i-1] = arr[i-1], arr[low] # swap with pivot element
    return i-1 

  

# Function to do Quick sort 
def quickSort(arr,low,high): 

    if (low < high): # no while here
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot + 1, high)
        
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
