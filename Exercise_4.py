'''
# Exercise_1 : Python code to implement merge sort.

# Description: Mergesort iterative and recursive algorithms.
               Input : Unsorted array
               Output: Sorted array in ascending order.

# Author: Neha Doiphode
# Date  : 06-19-2022

# Approach:
    Please refer to comments added in the code below.

# Time Complexity                            : T(n) = 2 * T(n/2)  Cost of spliting the array left and right parts
                                                      n           Cost of merging each half

                                               O(nlogn),
                                               for all 3 cases as the process of spliting the array
                                               and merging each half always happens.


# Space Complexity                           : O(n),
                                               Auxiliary array is needed for merging.

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this    : Nothing critical.
'''


def merge(left_half, right_half):

    # Exit condition
    if not left_half or not right_half:
        return (left_half or right_half)

    # Now, start merging
    l_ptr, r_ptr = 0, 0

    # Declare blank result array to store final merged array
    merged_result = []

    # Start looping
    # Condition for the loop is: loop until both halves are merged completely into result array
    # this is achieved by comparing length of result with len(left) + len(right)
    while len(merged_result) < (len(left_half) + len(right_half)):
        if left_half[l_ptr] < right_half[r_ptr]:
            merged_result.append(left_half[l_ptr])
            l_ptr += 1
        else:
            merged_result.append(right_half[r_ptr])
            r_ptr += 1

        if l_ptr == len(left_half):
            merged_result.extend(right_half[r_ptr:])

        elif r_ptr == len(right_half):
            merged_result.extend(left_half[l_ptr:])

    return merged_result


# Python program for implementation of MergeSort
def mergesort_recursive(arr):

    # Exit condition
    # Return when array contains single element
    if len(arr) < 2:
        return arr

    # To split the list into two halves, we need to find middle element index.
    middle = len(arr) // 2

    # recursive calls
    # python list slicing is half open ranged/upper bound exclusive,
    # middle element is excluded in the left half, it will be included in the right half
    # First sort all left halves until there is single element
    left_half  = mergesort_recursive(arr[:middle])

    # Now sort right half
    right_half = mergesort_recursive(arr[middle:])

    # Now start merging left and right halves
    return merge(left_half, right_half)

# Code to print the list
def printList(arr):
    print(arr)

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    arr = mergesort_recursive(arr)
    print("Merge sort recursive: Sorted array is: ", end="\n")
    printList(arr)
