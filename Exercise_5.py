# Python program for implementation of Quicksort
# timecomplexity: O(nlogn), space complexity: O(n)
# no issues faced while solving
# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = l-1
    x= arr[h]
    # find the correct position for the pivot element in the sorted array
    for j in range(l,h):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1


def quickSortIterative(arr, l, h):
    # store high and low indices of the give unsorted array in a stack
    length = h - l + 1
    list = [0] * length
    top = -1
    top += 1
    list[top] = l
    top += 1
    list[top] = h

    while top >= 0:

        part = partition( arr, l, h )
        # update stack with latest pivot data and run the loop until exhausted.
        if part-1 > l:
            top += 1
            list[top] = l
            top += 1
            list[top] = part - 1

        if part+1 < h:
            top += 1
            list[top] = part+1
            top+=1
            list[top] = h






