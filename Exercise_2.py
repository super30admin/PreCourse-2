# Python program for implementation of Quicksort Sort 
# Time complexity: o(nlogn) -> best case, o(n2) worst case
# Space complexity : o(n logn)

# give you explanation for the approach
def partition(arr,low,high):
   #pick the last element as pivot, 2 pointers for low and high. 
  
    #write your code here
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # last element is chosen as pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            # swap the elements 
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    #when pivot is placed in its correct position, return it
    return (i+1)
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) == 1:
        return arr

    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
