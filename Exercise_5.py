# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    i = (l-1)  # index of small element
    pivot = arr[h]

    for j in range(l, h):
        # if current element if smaller than or equal to pivot increment index of smaller element
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[h] = arr[h], arr[i+1]

    return (i+1)


def quickSortIterative(arr, l, h):
    # write your code here

    if l < h:

        p = partition(arr, l, h)
        # Sort separately elements before and after partition
        quickSortIterative(arr, l, p-1)
        quickSortIterative(arr, p+1, h)


# Driver Code
if __name__ == '__main__':

    arr = [4, 2, 6, 9, 2]
    n = len(arr)

    # Calling quickSort function
    quickSortIterative(arr, 0, n - 1)

    for i in range(n):
        print(arr[i], end=" ")
