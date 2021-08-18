# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    i = l
    j = h - 1
    pivot = arr[h]

    while i < j:
        while i < h and arr[i] < pivot:  # finds element which are bigger than pivot then stops
            i += 1
        while j > l and arr[j] >= pivot:  # finds element which are smaller than pivot then stops
            j -= 1
        if i < j:  # if pointers dont cross then swap
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:  # pivot is arr[h]
        arr[i], arr[h] = arr[h], arr[i]
    return i


def quickSortIterative(arr, l, h):
    # write your code here
    stack = [l, h]

    while len(stack) > 1:
        h = stack.pop()
        l = stack.pop()

        p = partition(arr, l, h)

        if p - 1 > l:
            stack.append(l)
            stack.append(p - 1)
        if p + 1 < h:
            stack.append(p + 1)
            stack.append(h)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
