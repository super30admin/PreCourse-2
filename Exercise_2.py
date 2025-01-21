# Python program for implementation of Quicksort Sort 
# Time complexity: worst: O(n^2) best: O(n long n)
# Space complexity : O(n)  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    i = low-1
    j = low
    pivot = arr[high]
    while i < j and j <= high - 1:
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j += 1

    i += 1
    temp = arr[i]
    arr[i] = arr[high]
    arr[high] = temp
    return i
    
    

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pivot_pos = partition(arr, low, high)

        quickSort(arr, low, pivot_pos-1)
        quickSort(arr, pivot_pos+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
