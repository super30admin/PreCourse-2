# Time Complexity : O(n^2)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# we choose a pivot point and compare numbers with the pivot
# need to change the position based on if the number is < or > pivot
# if we find an element < pivot, change it with first number > pivot
# keep repeating until we have sorted them

def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[high], arr[i + 1]) = (arr[i + 1], arr[high])
    return (i+1)
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        pivot_ele = partition(arr, low, high)
        quickSort(arr, low, pivot_ele - 1)
        quickSort(arr, pivot_ele + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
