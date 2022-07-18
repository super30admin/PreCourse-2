# Python program for implementation of Quicksort
# Time complexity - O(n^2) (Worst case)  
# Space complexity - O(logn)

# This function is same in both iterative and recursive
#  In this solution, the last element is taken as the pivot from the list and two pointers are defined. 
# The elements less than pivot and greater than pivot are swapped when the low element is greater than the higher one.
#  If the element low is greater than the higher one, we then swap the pivot and the higher one. Then we return the high element.
#  Then the pivot will be at its correct sorted position and its index is pi(partition index) which divides the array into two unsorted arrays to its left and right

def partition(arr, l, h):
    pivot_index = l
    pivot = arr[l]
    while l < h:
        while l < len(arr) and arr[l] <= pivot:
            l += 1
        while arr[h] > pivot:
            h -= 1
        if l < h:
            arr[l], arr[h] = arr[h], arr[l]
        arr[pivot_index], arr[h] = arr[h], arr[pivot_index]
    return h

def quickSortIterative(arr, l, h):
    stack = [(l, h)]
    while stack:
        l, h = stack.pop()
        pi = partition(arr, l, h)

        if pi - 1 > l:
            stack.append((l, pi - 1))

        if pi + 1 < h:
            stack.append((pi + 1, h))


arr = [1,4,3,2,5,4,3,6,7]
quickSortIterative(arr, 0, len(arr) - 1)
print(arr)