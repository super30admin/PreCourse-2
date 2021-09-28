Time Complexity : O(n^2)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

# Your code here along with comments explaining your approach

# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
def partition(arr,low,high):

def partition(arr,low,high): #Recursive way of implementing Quicksort. It takes last element as pivot, then put the pivot element at its correct position in sorted
# array, and places all smaller then pivot elements to left of pivot and all greater elements to right of pivot


    #write your code here

    i = (low-1) # index of smaller element
    pivot = arr[high] # pivot

    for j in range(low,high): # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i+1 # incrementing the index of smaller element
            arr[i], arr[j] = arr[j], arr[i] 

    arr[i+1] , arr[high] = arr[high] , arr[i+1]
    return (i+1)



# Function to do Quick sort 
def quickSort(arr,low,high): 

    #write your code here

    if len(arr) == 1:
        return arr
    if low < high: # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1) # Separately sorting elements before partition and after partition
        quickSort(arr, pi+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
