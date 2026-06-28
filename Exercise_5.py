# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
   #write your code here
    pivot = arr[h]
    i = l

    for j in range(l, h):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[h] = arr[h], arr[i]
    return i


def quickSortIterative(arr, l, h):
    # write your code here
    stack = [(l, h)]

    while stack:
        l, h = stack.pop()

        if l >= h:
            continue

        p = partition(arr, l, h)

        stack.append((l, p - 1))
        stack.append((p + 1, h))


# Driver code (NO INDENTATION)
arr = [10, 7, 8, 9, 1, 5]
quickSortIterative(arr, 0, len(arr) - 1)
print(arr)

# TC - O(nlogn)
# SC - O(logn) - average O(n^2) worst case