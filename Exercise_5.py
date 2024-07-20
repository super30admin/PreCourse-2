# Time Complexity : O(n log n) on average, O(n^2) in the worst case
# Space Complexity : O(log n) for the stack space
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : No
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #Write your code here
    # Choosing the rightmost element as pivot
    pivot = arr[h]
    i = l - 1  # Index of smaller element
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[h] = arr[h], arr[i + 1]  # Place pivot in the correct position
    return i + 1

def quickSortIterative(arr, l, h):
    #Write your code here
    # Create a stack for storing subarray indices
    stack = [(l, h)]
    while stack:
        l, h = stack.pop()
        if l < h:
            # Partition the array and get the index of the pivot
            p = partition(arr, l, h)
            # Push left and right subarrays to stack
            if l < p - 1:
                stack.append((l, p - 1))
            if p + 1 < h:
                stack.append((p + 1, h))

# Code to print the list
def printList(arr):
    for i in arr:
        print(i, end=" ")

    print()

# Driver code to test the above code
if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array is:", end="\n")
    printList(arr)
    quickSortIterative(arr, 0, len(arr) - 1)
    print("Sorted array is:", end="\n")
    printList(arr)
