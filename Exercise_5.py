# Python program for implementation of Quicksort
# Time Complexity - O(n*log(n)) for best and average cases.
#                   O(n^2) for worst case when the given array is already sorted.
# Space Complexity - O(log*n)

# This function is same in both iterative and recursive
# below used partition is Hoare's partition.
# in this partition first element is picked as the pivot and two pointers are defines low and high
# low starts from 0 and traverses through the list until it finds the element > than pivot element
# then end starts from end of the array and traverses through the list until it finds the element < pivot element
# once we have elements > and < pivot, we swap those elements if low < end
# else if low > end we swap the element at pivot position with the element at end position and return the end position
# Now the element at pivot position is at its correct sorted position in the array and its index is called as pi(partition index)
# pi divides the array into 2 unsorted arrays to its left and right
def partition(arr, l, h):
    pivot_index = l
    pivot = arr[l]
    while l < h:
        while l < len(arr) and arr[l] <= pivot:
            l += 1
        while arr[h] > pivot:
            h -= 1
        if l < h:
            arr[l], arr[h] = arr[h], arr[l]
        arr[pivot_index], arr[h] = arr[h], arr[pivot_index]
    return h


# instead of using recursive method we created a stack which stores the indices of the start and end position
# sort the pivot position using above described hoare partition
def quickSortIterative(arr, l, h):
    stack = [(l, h)]
    while stack:
        l, h = stack.pop()
        pi = partition(arr, l, h)

        # no need to do partition if l and partition index is same or less than start index
        if pi - 1 > l:
            stack.append((l, pi - 1))
        # no need to do partition if h and partition index is same or greater than end index
        if pi + 1 < h:
            stack.append((pi + 1, h))


arr = [4, 3, 5, 2, 1, 3, 2, 3]
quickSortIterative(arr, 0, len(arr) - 1)
print(arr)
