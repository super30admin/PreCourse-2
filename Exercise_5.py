# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    i = (low - 1)  # intiate to index that can be considered from the beginning of array
    pivot = arr[high] # pick any pivot. Here we pick from the end

    for j in range(low, high):
        # check if current element is less than the pivot.
        if arr[j] <= pivot:
            i += 1
            # keep swapping these places till we reach arr[low] < arr[high] for every recursive array search
            arr[i], arr[j] = arr[j], arr[i]
    # swap the element with index at high as that is the actual secured place of element in array
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)

    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1


        p = partition(arr, l, h)
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


# Driver code
arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
    print ("% d" % arr[i]),


