# Time Complexity : O(nlog(n)) Average case, O(n^2) worst case
#  Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Also worked locally
# Any problem you faced while coding this : No
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    j = low + 1
    for i in range(low+1, high+1): 
        if arr[i] < arr[low]:
            arr[j], arr[i] = arr[i], arr[j] 
            j +=1 
    arr[low], arr[j-1] =  arr[j-1], arr[low]
    return j-1

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low >= high: return 
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot-1)
    quickSort(arr, pivot+1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
