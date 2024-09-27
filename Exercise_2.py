# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
'''
Approach:
1) Choose a pivot and swap elements of the array such that the elements to the left of the pivot are always lesser
and the elements to the right of pivot are always greater than pivot.
2) At this point, the pivot element will be at its correct position
3) Now partition the array into 2 sub arrays, one to the left of pivot and the other to its right
4) apply the above steps to both sub arrays
5) break the loop when the arrays can no more be partitioned
'''
def partition(arr,low,high):
    #write your code here
    pivot = high
    pivot_index = low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i],arr[pivot_index] = arr[pivot_index], arr[i]
            pivot_index += 1
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return pivot_index
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low >= high:
        return

    p = partition(arr, low, high)
    quickSort(arr, low, p-1)
    quickSort(arr, p+1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end = " "),
  
 
"""
n = number of elements in the array
Space Complexity: O(1) ignoring the recursion stack 

Time Complexity:
O(n log n)
"""