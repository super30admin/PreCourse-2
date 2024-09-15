# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    pivot = arr[high]
    index = low - 1
    for i in range(low, high):
        if arr[i] < pivot:
            index += 1
            # Swapping the large with small values
            temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp
    temp = arr[index + 1]
    arr[index + 1] = arr[high]
    arr[high] = temp
    return index + 1

def quickSortIterative(arr, low, high):
    stack = []
    stack.append(low)
    stack.append(high)
    while stack:
        high = stack.pop(-1)
        low = stack.pop(-1)
        if (high-low) >1:
            partition_index = partition(arr,low,high)
            stack.append(low)
            stack.append(partition_index-1)
            stack.append(partition_index+1)
            stack.append(high)
    print("Sorted Array: " , arr)

quickSortIterative([20,4,2,3,6,19],0,5)

# Complexity

# Time Complexity -   nlog(n) worst case o(n^2) if the array is already sorted
# Space Complexity - o(1) as iam  not using the extra space
