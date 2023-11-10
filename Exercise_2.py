# Python program for implementation of Quicksort Sort 
# // Time Complexity : O(nlogn)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Not found
# // Any problem you faced while coding this : There was a confusion between quick sort and iterative quick sort

# give you explanation for the approach
# Take two points i and j, low and high as start and end points resp.
# Keep moving forward with the loop and compare with the pivot, swap if i is less than j.
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while(i<j):
        if arr[i]<=pivot:
            i+=1
        if arr[j]>=pivot:
            j-=1
        if (i<j):
            (arr[i],arr[j]) = (arr[j],arr[i])
    (arr[low],arr[high]) = (arr[high],arr[low])
    return j
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if (low<high):
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
  
 
