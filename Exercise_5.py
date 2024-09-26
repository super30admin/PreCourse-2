'''
Iterative Quick Sort : In-place sorting

Time Complexity:
    partition(): O(n)
    quicksortIterative(): In the worst case, the pivot is always the edge element in the array, causing the while loop to iterate ~n times.
                          In each such iteration, calls partition once.
                          Thus, O(n^2)

Space Complexity:
partition(): O(1)
quicksortIterative(): In the worst case, needs to add ~every single consecutive pair to the stack, thus increasing the auxiliary space by a proportional amount of ~n.
                      Hence O(n)

Issue while implementing: Yes, iterative approach was new to me but understood after spending some time studying and visualizing on paper.
'''


# This function is same in both iterative and recursive implementations of quicksort.
def partition(arr, low, high):
    '''
    :param arr: an array which needs to be sorted using quicksort
    :param low: the lowest index value of the passed array arr in terms of the original array indexing
    :param high: the highest index value of the passed array arr in terms of the original array indexing
    :return: an index position for the pivot element that separates arr into two halves while placing the pivot element in its sorted position
    '''

    pivot_element = arr[high]

    index_to_store_elem_less_than_pivot = low

    for idx in range(low, high):
        if arr[idx] < pivot_element:
            arr[index_to_store_elem_less_than_pivot], arr[idx] = arr[idx], arr[index_to_store_elem_less_than_pivot]

            # Now that this element has been placed before the pivot, we need to move to the next position
            index_to_store_elem_less_than_pivot += 1

    # Put the pivot element that is at the end of the array to its correct sorted position
    arr[high], arr[index_to_store_elem_less_than_pivot] = arr[index_to_store_elem_less_than_pivot], arr[high]

    # return this position that contains the sorted element, now we can sort the two halves of the array independently
    return index_to_store_elem_less_than_pivot


def quickSortIterative(arr, l, h):
    from collections import deque

    # Maintain a stack data structure that stores sub-arrays that need to be sorted.
    quick_sort_stack = deque()
    quick_sort_stack.append((l, h))

    # Iteratively take
    while quick_sort_stack:
        sub_array_start_position, sub_array_end_position = quick_sort_stack.pop()
        pivot_position = partition(arr, sub_array_start_position, sub_array_end_position)

        # The element at pivot_position is already at its correct position. Need to sort the two halves now.

        # Push the sub-arrays that are to the left and the right of this pivot to the stack
        # (but only if elements at those positions are not already sorted)
        if pivot_position - 1 > sub_array_start_position:
            # means that the pivot element is not the leftmost element in the left subarray
            quick_sort_stack.append((sub_array_start_position, pivot_position - 1))
        if pivot_position + 1 < sub_array_end_position:
            # means that the pivot element is not the rightmost element in the right subarray
            quick_sort_stack.append((pivot_position + 1, sub_array_end_position))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
