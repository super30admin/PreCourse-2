# // Time Complexity : O(NlogN)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
"""
1. get the right postition for the ptivot element by calling partition function
2. partition function will calculate the pivot index as midpoint of the given array
3. swap the pivot element with rightmost element
4. traverse through an array compare each element with if its less than right most element swap it with low and each
5. at the end swap low with rightmost element , here low is right position for the pivot element return low
6. using pivot index value call quick sort for left and right halves of the array Recursively
"""


# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    # write your code here
    pivot = (low + high) // 2
    arr[pivot], arr[high] = arr[high], arr[pivot]

    for each in range(low, high):
        if arr[each] <= arr[high]:
            arr[each], arr[low] = arr[low], arr[each]
            low += 1
    arr[low], arr[high] = arr[high], arr[low]
    return low


# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here
    if low >= high:
        return
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


