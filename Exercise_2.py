# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# It returns location of x in given array arr  
# if present, else returns -1 
# // Time Complexity : O(log(n))
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# This function is same in both iterative and recursive
# It returns location of x in given array arr  
# if present, else returns -1 
# // Time Complexity : Best - O(nlog(n)), Worst - O(n^2)
# // Space Complexity : O(log(n))
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

def partition(arr,low,high):
    i = low-1 
    pivot = arr[high] 
    for j in range(low , high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
    
# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
      m = partition(arr,low,high)
      quickSort(arr,low,m-1)
      quickSort(arr,m+1,high) 
    
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
