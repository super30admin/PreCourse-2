# Time Complexity : O(nlogn): It follows Divide and Conquer. Breaks down problem into smaller sub problems
# Space Complexity : O(n)

# Approach: Merge Sort would break down the original array into smaller and smaller portions, until the portions are of size 1

# Then we begin the Merge Process, based on the smaller element between the two comparators.

# Python program for implementation of MergeSort
def merge(arr, left, middle, right):

    """

    Function to Merge 2 arrays

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    i = j = 0

    # Break down the array into Left and Right Halves

    Left = arr[left : middle + 1]
    Right = arr[middle + 1 : right + 1]

    N = len(Left)
    M = len(Right)

    # We begin with an index starting at the Left location, because that is the smaller of the two pointers (Left & right)
    k = left

    while i < N and j < M:

        # Compare and Merge

        if Left[i] <= Right[j]:
            arr[k] = Left[i]
            i += 1
            k += 1
        else:
            arr[k] = Right[j]
            j += 1
            k += 1

    # There could still be leftover elements. We are checking that here
    while i < N:
        arr[k] = Left[i]
        i += 1
        k += 1
    while j < M:
        arr[k] = Right[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    """
    Function to Perform MergeSort

    Time Complexity: O(logn)
    Space Complexity: O(1)
    """
    # write your code here

    if right <= left:
        return "Done"

    mid = (left + right) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)
    merge(arr, left, mid, right)


# Code to print the list
def printList(arr):

    # write your code here
    for i in range(len(arr)):
        print("{}, ".format(arr[i]))
    print("\n")


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 7, 4]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array is: ", end="\n")
    printList(arr)
