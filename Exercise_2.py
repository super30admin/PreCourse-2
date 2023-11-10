# Time Complexity : O[n]
# Space Complexity : O(1)
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot_index = low
    pivot = arr[pivot_index]

    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low+=1
        while arr[high] > pivot:
            high-=1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return high
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)
  
 
