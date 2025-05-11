# Time Complexity : O(n log n) on average, O(n^2) in the worst case
# Space Complexity : O(log n) on average for the stack, O(n) in the worst case
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : YES, a little. I adapted my recursive solution to an iterative one and had to manage my own stack

# This function is same in both iterative and recursive
def partition(arr, l, h):
  # choose the last element as pivot
    pivot = arr[h]
    # i will mark the end of the smaller-than-pivot region
    i = l - 1

    # move all elements <= pivot to the front
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot right after the smaller elements
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    # return pivot’s final index
    return i + 1


def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * size
    top = -1


    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:
        # pop a range to sort
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # partition the range and get pivot index
        p = partition(arr, l, h)

        # if there are elements on the left side of pivot, push that range
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        # if there are elements on the right side of pivot, push that range
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h
  

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    quickSortIterative(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
