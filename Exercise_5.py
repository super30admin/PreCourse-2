# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    pivot = arr[l]
    i = l + 1
    j = h

    while (i < j):
        while (i <= j and arr[i] < pivot):
            i = i + 1

        while (i <= j and arr[j] > pivot):
            j = j - 1

        if (i < j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[l]
    arr[l] = arr[j]
    arr[j] = temp
    return j


def quickSortIterative(arr, l, h):
    # write your code here
    stack = []
    stack.append(l)
    stack.append(h)

    while len(stack) > 0:
        high = stack.pop()
        low = stack.pop()
        pivot = partition(arr, low, high)
        if (pivot + 1) < high:
            stack.append(pivot + 1)
            stack.append(high)
        if low < (pivot - 1):
            stack.append(low)
            stack.append(pivot - 1)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
