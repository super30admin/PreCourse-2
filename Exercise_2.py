# Time Complexity : O(n^2)
# Space Complexity : O(log(n))
# Did this code successfully run on Leetcode : N.A.
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Python program for implementation of Quicksort Sort
  
# give you explanation for the approach

# used last element as pivot and swapped every element
# less than the pivot with a counter variable which starts at 0
def partition(arr,low,high):
    pivot = arr[high]
    mid = low - 1

    for i in range(low, high):
        if arr[i] <= pivot:
            mid += 1
            # swap mid, i
            arr[mid], arr[i] = arr[i], arr[mid]

    # swap mid+1, high-1
    arr[mid+1], arr[high] = arr[high], arr[mid+1]
    return mid + 1


# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print ("Given array is")
print(arr)
quickSort(arr,0,n-1) 
print ("Sorted array is:")
print arr

