# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    left = l + 1
    right = h
    if right <= left:
        return None
    pivot = arr[l]
    while right >= left:
        while right > left and arr[right] >= pivot:
            right -= 1
        while left < right and arr[left] <= pivot:
            left += 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        elif left == right:
            if arr[left] <= pivot:
                arr[l], arr[left] = arr[left], arr[l]
                pivot = arr[l]
        else:
            break
        right -= 1
    return left


def quickSortIterative(arr, l, h):
    # write your code here
    sorted_arr = [None] * len(arr)
    left = l
    right = h
    pivot_l = pivot_r = partition(arr, l, h)
    if pivot_l is None:
        sorted_arr[:] = arr[:]
    else:
        while pivot_l is not None:
            pivot_l = partition(arr, left, right)
            if pivot_l is None:
                break
            sorted_arr[pivot_l] = arr[pivot_l]
            right = pivot_l - 1
        left = pivot_r + 1
        right = h
        if left <= right:
            while pivot_r is not None:
                pivot_r = partition(arr, left, right)
                if pivot_r is None:
                    break
                sorted_arr[pivot_r] = arr[pivot_r]
                left = pivot_r + 1
        else:
            sorted_arr[pivot_r:] = arr[pivot_r:]

    arr = sorted_arr


# Driver code to test above
arr = [4, 5, 0, 50, 10, 80, 11, 23, 0]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
