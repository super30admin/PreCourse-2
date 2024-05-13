# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
     #write your code here
    pivot = arr[h]  # Choosing the pivot as the last element
    i = l - 1  # Index of smaller element

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1




def quickSortIterative(arr, l, h):

    stack = []

    top = -1

    # Push initial values of l and h to stack
    top += 1
    stack.append(l)
    top += 1
    stack.append(h)

    # Keep popping from stack while it is not empty
    while top >= 0:
        # Pop h and l
        h = stack.pop()
        l = stack.pop()

        # Set pivot element at its correct position
        p = partition(arr, l, h)

        # If there are elements on the left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top += 1
            stack.append(l)
            top += 1
            stack.append(p - 1)

        # If there are elements on the right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top += 1
            stack.append(p + 1)
            top += 1
            stack.append(h)


# Driver code to test the above functions
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

print("Given array is:")
print(arr)

quickSortIterative(arr, 0, n - 1)

print("Sorted array is:")
print(arr)

