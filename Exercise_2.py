# Python program for implementation of Quicksort Sort
# Time Complexity : O(n*log n)
# Space Complexity : O(n*log n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : None

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[low] # considering first element as pivot
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot:  # while left element is less than or equal to right and less than or equal to pivot element
            left += 1
        while left <= right and arr[right] >= pivot: # while right element is greater than or equal to left and greater than or equal to pivot element
            right -= 1
        if right < left: # loop breaks when right element becomes less than left
            break
        else:
            arr[left],arr[right] = arr[right],arr[left] # initialising left to right and vice-versa
    arr[low],arr[right] = arr[right],arr[low]
    return right


# Function to do Quick sort
def quickSort(arr,low,high):

    #write your code here
    if low < high:
        part = partition(arr,low,high)
        quickSort(arr,low,part - 1)  # using recursive method for sorting left part of  the list
        quickSort(arr,part + 1,high) # using recursive method for sorting right part of the list

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
print(arr)
