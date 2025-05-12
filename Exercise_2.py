# Time Complexity: O(n log n) on average, O(n^2) in the worst case
# Space Complexity: O(log n) due to recursion stack

# Any problem you faced while coding this: 
# It was a bit tricky to understand partition logic in the beginning

# Python program for implementation of Quicksort Sort

def partition(arr, low, high):
    pivot = arr[high]  # Picking the last element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
            print("Swapping because", arr[i], "<", pivot, "->", arr)
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    print("Moving pivot", pivot, "->", arr)
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print("Partition index:", pi)

        quickSort(arr, low, pi - 1)  # Recursively sort left
        quickSort(arr, pi + 1, high)  # Recursively sort right

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("Original array:", arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
