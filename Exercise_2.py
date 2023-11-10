# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
"""
Rasika Sasturkar
We choose the last element as pivot and find the position
where we can partition the array, and then call quicksort
on the respective halves of the partition.
Time Complexity: O(nlogn) - average case, O(n^2) - worst case
Space Complexity: O(1)
"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Function to do Quick sort 
def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)


# Driver code to test above
def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i]),


if __name__ == "__main__":
    main()
