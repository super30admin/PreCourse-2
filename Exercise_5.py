# Python program for implementation of Quicksort

# Time complexity:
# 1) best/aveg case: O(nlog n) because array will be divided into equaly roghly same size subarrays and stack will process them iteratively
# 2) worst case: O(n^2) when pivot is either smallest or the largest element

# space complexity:
# 1) best case: O(log n): stack size/depth
# 2) worst case: O(n) : when stack depth is linear


# This function is same in both iterative and recursive
# just for the partition
def partition(arr, low, high):
    # write your code here
    pivot = arr[low]  # choosing pivot as the first element of an array
    i = low  # Moves from left to right, looking for elements greater than pivot
    j = high  # Moves from right to left. looking for elements smaller than pivot

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1  # incrementing i untill current element is less than or equals to pivot
        while arr[j] > pivot and j >= low + 1:
            j -= 1  # decrementing j untill current element is greater than pivot
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # swap elements at i and j
    arr[low], arr[j] = (
        arr[j],
        arr[low],
    )  # swap pivot with j that makes pivot at the right place and all the elements on the right side will be greater than j and left side smaller
    return j  # Return the pivot index


def quickSortIterative(arr, low, high):
    # write your code here
    # using stack to store sub array indices and to process them iteratively, with same partitioning logic used in recursive approach
    stack = []
    stack.append((low, high))  # push the initial low,high values onto stack
    while stack:
        low, high = stack.pop()  # pop the topmost elements for indices
        p_index = partition(arr, low, high)  # find pivot and do partitioning
        if p_index - 1 > low:
            stack.append((low, p_index - 1))  # push left subarray into stack
        if p_index + 1 < high:
            stack.append((p_index + 1, high))  # push right subarray into stack


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
