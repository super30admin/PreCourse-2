# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
#Time Complexity = O(n^2) - worst case, O(nlogn) - best case
#Space Complexity = O(logn)

def partition(arr, l, h):
    pivot = arr[h]  # assigning pivot as last element

    i = l - 1  # pointer i to index -1

    for j in range(l, h):  # run j pointer from start to end of arr
        if arr[j] < pivot:  # each time checking if current element is less than pivot
            i = i + 1  # if yes keep incrementing i pointer
            arr[i], arr[j] = arr[j], arr[
                i]  # and swap elements - To make 2 groups (1st grp = elements less then pivot, 2nd grp = elements less then pivot)

    arr[i + 1], arr[h] = arr[h], arr[
        i + 1]  # At last swap element i+1 index with pivot element - Now pivot element comes in middle

    return i + 1  # returning index of pivot

def quickSortIterative(arr, l, h):
    size = h - l + 1 # Stack creation
    stack = [0] * (size)
    top = -1

    top = top + 1 # pushing the initial values
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0: # pop values to find pivot

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, h) #to find the pivot element

        if p - 1 > l: # sorting elements in left portion - setting new values for l and h
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h: # sorting elements in right portion - setting new values for l and h
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

