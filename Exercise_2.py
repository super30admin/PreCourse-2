'''
# Exercise_2 : Python program for the implementation of Quicksort.

# Description: Quick sort recursive. algorithm.
               Returns sorted array in ascending order.

# Author: Neha Doiphode
# Date  : 06-17-2022

# Approach:
    * Quicksort uses divide and conquer technique.
    * Quicksort picks an element as pivot and partitions the array around pivot element such that,
      elements to the left of pivot are lesser than pivot and elements to the right are greater than pivot.
    * New pivots are chosen for the left and right halves and the process is repeated until the entire array is sorted.
    * Several ways exist to choose pivot element.
        - First element of the array can be chosen as pivot.
        - Last element of the array can be chosen as pivot.
        - Random element can be chosen as pivot.
        - Median of three elements can be chosen as pivot.

    * Below approach uses last element as pivot.


# Time Complexity                            : T(n) = 2 * T(n/2)  Cost of spliting the array into left and right parts
                                                      n           Cost of partitioning the array

                                               O(nlogn)
                                               Average case = O(nlogn)
                                               Worst case   = O(n^2) When pivot is always smallest or largest element,
                                                              then the partiion always contain n-1 elements.
                                                              So, it will be n + (n-1) + (n-2) +....0
                                                                  which is nothing but gauss sum = n(n+1) / 2 = O(n^2)

# Space Complexity                           : O(log n),
                                               quick sort makes use of tail recursion where,
                                               partitioning process happens before the recursive call so,
                                               a lot of space optimization can be done with each recursive call.

# Did this code successfully run on Leetcode : Did not run on leetcode.
# Any problem you faced while coding this    : Nothing critical.
'''

def partition(arr,low,high):
    left = low - 1
    pivot = arr[high]

    for right in range(low, high):
        if arr[right] <= pivot:
            left += 1
            arr[left], arr[right] = arr[right], arr[left]

    arr[left + 1], arr[high] = arr[high], arr[left + 1]
    return left + 1

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
        p_index = partition(arr, low, high)
        quickSort(arr, low, p_index - 1)
        quickSort(arr, p_index + 1, high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]

n = len(arr)
quickSort(arr,0,n-1)
print (f"Sorted array is: {arr}")
