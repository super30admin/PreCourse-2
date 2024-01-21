# Time Complexity : Average case: O(nLogn) where n is the size of the array
# Space Complexity : O(n) where n is the size of the array
# Did this code successfully run on Leetcode : No
# Any problem you faced while coding this : Hard to find this concept online


# Python program for implementation of Quicksort
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# This function is same in both iterative and recursive
def partition(arr, low, high):
    # write your code here
    # using Lomuto parititon; assuming pivot is at the end
    pivot = arr[high]
    # keeping track of lower elements using i and higher elements between i and j
    # initially assuming elements left to i are smaller than pivot
    i = low - 1

    for index in range(low, high):
        # elements right of i and left of j are higher
        if arr[index] > pivot:
            continue

        i += 1
        swap(arr, i, index)

    # swap pivot with it's correct position
    swap(arr, i + 1, high)
    return i + 1


def quickSortIterative(arr, l, h):
    # write your code here
    stack = []
    """
    stack will always have pairs of two stored
    top one is end index and bottom one is start index
    we get the partition index using these two
    we do subsequent stack push if the values are valid
    """

    stack.append(l)
    stack.append(h)

    while len(stack):
        end = stack.pop()
        start = stack.pop()

        partitionIndex = partition(arr, start, end)

        # left side of array needs to have atleast one element
        if partitionIndex - 1 > start:
            stack.append(start)
            stack.append(partitionIndex - 1)

        # right side of array needs to have atleast one element
        if partitionIndex + 1 < end:
            stack.append(partitionIndex + 1)
            stack.append(end)
