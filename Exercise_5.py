# Python program for implementation of Quicksort

# Time Complexity = O(n logn)
# space complexity = O(n)
def partition(arr, l, h):
    mid = (l + h) / 2
    mid_element = arr[mid]

    while l < h:

        while arr[l] <= mid_element and l < len(arr):
            l += 1

        while arr[h] > mid_element:
            h -= 1

        if l < h:
            arr[l], arr[h] = arr[h], arr[l]

    arr[h], arr[mid] = arr[mid], arr[h]

    return h


def quickSortIterative(arr, l, h):
    #  defining stack and its size
    stack_size = len(arr) - 1
    stack_array = [0] * stack_size
    # initializing top of stack and pushing low and high
    top_pointer = -1

    top_pointer = top_pointer + 1
    stack_array[top_pointer] = l
    top_pointer = top_pointer + 1
    stack_array[top_pointer] = h

    while top_pointer >= 0:
        # iterate in stack till top is greater than 0
        h = stack_array[top_pointer]
        top_pointer = top_pointer - 1
        l = stack_array[top_pointer]
        top_pointer = top_pointer - 1

        # Get pivot element with current low and high of stack

        current_pivot = partition(arr, l, h)

        #  based on the current pivot element manage the low and high in stack and move according
        if current_pivot - 1 > l:
            top_pointer = top_pointer + 1
            stack_array[top_pointer] = l
            top_pointer = top_pointer + 1
            stack_array[top_pointer] = current_pivot - 1
        elif current_pivot + 1 < h:
            top_pointer = top_pointer + 1
            stack_array[top_pointer] = current_pivot + 1
            top_pointer = top_pointer + 1
            stack_array[top_pointer] = h

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print (arr[i])

