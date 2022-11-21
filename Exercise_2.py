# Time Complexity : best and avg case time is O(n log n) when pivot is choosen as middle elem or when array elements are in disordered sequence
#                   worst case time is O(n^2) when we choose the largest or smallest element as the pivot 
# Space Complexity : O(1) space
# Did this code successfully run on Leetcode : Did not try running code on leetcode as the question is bit different.
# Any problem you faced while coding this : No issues faced


# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]                                   #taking last element as the pivot
    i, j = low, high - 1
    while i < j:
        while i < high and arr[i] < pivot:              # i looks for element bigger than pivot, if elem at i < pivot then i is incremented
            i += 1                                      
        while j > low and arr[j] >= pivot:              # j looks for element smaller than pivot, if elem at j >= pivot then j is decremented
            j -= 1
        
        if i < j:                                       # if i < j then we swap the elements at i and j         
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:                                  
        arr[i], arr[high] = arr[high], arr[i]

    return i                                            # returns the index of pivot where elements on left of i are less than pivot
                                                        # and elements to right of i are greaterd than pivot

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        pivot = partition(arr, low, high)               # we call partition function that returns the index of pivot
        quickSort(arr, low, pivot-1)                    # recursively call quicksort on left subarrray
        quickSort(arr, pivot+1, high)                   # recursively call quicksort on right subarray


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
