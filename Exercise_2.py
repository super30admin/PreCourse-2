"""
Runtime Complexity:
1) The runtime of the quicksort algorithm mainly depends on the partiton function used. Because we just call quicksort recursively which invokes the partition.
2) The partition algorithm, assigns the pivot to the last element. And compares each element with the pivot and arranges all the elements lesser than the pivot to the left and
larger elements to the right.
3) Therefore, the runtime of the algorithm is O(n).

Space Complexity:
O(n) as 'n' is the number of elements to be sorted and n operation are computed recursively.

- Yes, the solution worked on leetcode.
Idea - assign a pivot pointer. This can be done to first, last, middle elements. The main goal is to partiton the given set into equal halves and compare. Worst case happens when pivot is chosen
as smallest element because this will lead to a partition with n-1 and 1 elements. The other recursion goes on with no elements to sort.
"""

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    i  = low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i], arr[j]  = arr[j], arr[i]
        arr[high],arr[i+1] = arr[i+1], arr[high]
    return i+1
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        q = partition(arr,low,high)
        quickSort(arr,low,q-1)
        quickSort(arr,q+1,high)
    
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
