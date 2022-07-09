# Python program for implementation of Quicksort Sort
# Time Complexity : O(nlogn): It follows Divide and Conquer. Breaks down problem into smaller sub problems
# Space Complexity : O(n) : Please can you explain if this is correct?
# Approach:

# I pick the Pivot as the First Element, Left pointer would be Low + 1, Right would be High
# Then, the right pointer keeps decreasing until we find an element less than pivot. In case we get the element, the left pointer increases until we find the first element greater than Pivot. Then we swap
# If the Left pointer and right pointer meet, we compare that element with Pivot. If it's less, we swap the pivot and the meeting location.
# The code repeats then by decreasing the right pointer. The checking condition being Left should be Less than Right

# The return value from the Partition function would be location of the pivot, governed by Arr{low}. The code returns when Left and Right pointer meet each other.

from tkinter import N


def partition(arr, low, high):

    """

    Function to do the computation of swapping the elements for QS

    Time Complexity: O(n)
    Space Complexity: O(1)

    """

    # write your code here
    pivot = arr[low]
    left = low
    right = high
    while right >= left:

        while right > left and arr[right] >= pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1
        if left == right:
            if arr[left] <= pivot:
                arr[low], arr[left] = arr[left], arr[low]
                pivot = arr[low]
        elif left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
        right -= 1
    return left


# Function to do Quick sort
def quickSort(arr, low, high):
    """
    Recursive Function to Perform Quicksort

    Time Complexity: O(logn). Worst Case O(n ^ 2)
    Space Complexity: O(n) ? Please can you confirm?

    """

    # write your code here
    if low >= high:
        return "End"
    else:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    return "End"


# Driver code to test above
arr = [50, 100, 0, 111, 23, 0, 4, 1]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
