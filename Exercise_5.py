# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # pivot is chosen at the last element

    pivot = arr[h]
    # greater element is initialized
    greater_element = l-1

    for j in range(l,h):
        if arr[j] <= pivot:
            # If the element is less than pivot swap it with greater element
            greater_element = greater_element + 1
            arr[greater_element],arr[j] = arr[j], arr[greater_element]

    # Swap the greater element and the pivot
    arr[greater_element+1],arr[h] = arr[h], arr[greater_element+1]
    # return the partitioning index
    return greater_element+1


def quickSortIterative(arr, l, h):
    length_array = h - l + 1
    # l and h are added as a tuple to the stack, it has the low and high index of the subarray that requires sorting
    sorting_stack = [(l, h)]

    while sorting_stack:
        low, high = sorting_stack.pop()

        index = partition(arr, low, high)

        if index - 1 > low:
            # it indicates the left subarray requires sorting
            sorting_stack.append((low, index - 1))

        if index + 1 < high:
            # it indicates the right subarray requires sorting
            sorting_stack.append((index + 1, high))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),