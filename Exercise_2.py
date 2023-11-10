# Python program for implementation of Quicksort Sort 

# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Any problem you faced while coding this :no

# give you explanation for the approach
def partition(arr,low,high):
    #choosing right most elem as pivot
    pivot = arr[high]
    i = low - 1
    for k in range(low, high):
        if arr[k] <= pivot: #if the elem smaller then pivot is found then swap i and kth and increase ith pointer
            i = i+1
            #swap the elements
            arr[i],arr[k] = arr[k], arr[i]
    #swap the pivot elem with the larger element
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high :
        # partition index
        x  = partition(arr, low, high)
        # calling left side
        quickSort(arr, low, x-1)
        # calling right side
        quickSort(arr,x+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])