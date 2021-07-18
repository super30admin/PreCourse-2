# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
'''
Select a pivot element, in our case, first element of the considered array
Arrange elements such that, 
    all elements less than pivot are arranged (swapped) to the left 
    all elements greater than pivot are arranged (swapped) to the right
    place pivot between these left and right "partitions"
    (this is the position of the pivot element in the sorted order)
Recurse similarly on the left and right partition

- find first index from left where elem > pivot
- find first index from right where elem < pivot
- swap and continue moving inwards till left crosses 
- place pivot on the crossed right index
- recurse on the two partitions
'''
def partition(arr,low,high):
  
    #write your code here
    pivot, pivot_idx = arr[low], low
    low = low+1
    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[high], arr[pivot_idx] = arr[pivot_idx], arr[high]
    return high

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pivot_pos = partition(arr, low, high)
        quickSort(arr, low, pivot_pos-1)
        quickSort(arr, pivot_pos+1, high)
    return arr
    

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  

'''
Time complexity: O(N^2) - worst case when every time we pick the smallest elem as pivot i.e. array is already sorted
Average time complexity (for randomly shuffled array) - O(NlogN)

Space complexity: O(1)
'''