# Time Complexity - O(n log n)
# Space Complexity - O(1)
# Python program for implementation of Quicksort Sort 
  
def swap(index1, index2, arr):
    arr[index1], arr[index2] = arr[index2], arr[index1]  

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    index = low
    pivot = arr[index]

    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
    
        while arr[high] > pivot:
            high -= 1
    
        if low < high:
            swap(low, high, arr)

    swap(index, high, arr)
    
    return high

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        index = partition(arr, low, high)
        quickSort(arr, low, index - 1)
        quickSort(arr, index + 1, high)


    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
