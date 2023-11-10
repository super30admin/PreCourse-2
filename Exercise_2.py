# Python program for implementation of Quicksort Sort 
"""
Runtime Complexity:
- The quick sort algorithm is mainly dominated by partition function. The partiton() runs a loop from the start to the end of the list.  Therefore the overall complexity is O(n).
- The algorithm chooses the last element as the pivot, and compares with all elements in the list and swaps smaller elements to the left of the pivot and greater elements to the right.

-Yes, the code worked on leetcode
"""
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i = i+1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
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
  
 
