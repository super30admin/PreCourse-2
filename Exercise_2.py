# Time complexity - O(n log n)
# Space complexity - O(log n)
# Code runs properly

# Approach:
# Quick sort is a divide and conquer algorithm.
# I choose the end as pivot and partitioned the array with elements less than the pivot and elements more than the pivot, and used recursion to partition the
# array until the arrays can't be partitioned anymore. When arrays can't be partitioned anymore, the array will be sorted and then combined to form the sorted array.

def partition(arr,low,high):
    pivot = arr[high]
    index = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            index+= 1
            arr[index], arr[j] = arr[j], arr[index]
    index+= 1        
    arr[index], arr[high] = arr[high], arr[index]
    return index
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if high <= low:
        return 
    pivot = partition(arr,low,high)
    quickSort(arr, low, pivot - 1)
    quickSort(arr,pivot + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:",arr) 
