# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    # write your code here

    pivot = arr[low]
    i, j = low, high

    while i < j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if j >= low:
        arr[low], arr[j] = arr[j], arr[low]
        return j

    return low


def quickSortIterative(arr, l, h):
    # write your code here
    stack = [l, h]

    while stack:
        y = stack.pop()
        x = stack.pop()

        p = partition(arr, x, y)


        if p - 1 > x:
            stack.append(x)
            stack.append(p-1)

        if p + 1 < y:
            stack.append(p+1)
            stack.append(y)

# Driver code to test above
arr = [1, 5, 8, 9, 7, 10]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
