# Python program for implementation of Quicksort Sort 

"""
Approach --
1. Use a pivot element to swap rest pf the elements around it
2. Use a pointer element to keep track smaller elements
3. Swap elements smaller than pivot element in the front
4. Continue till the end of the list

Time complexity - 0(n log n)
Space complexity - O(n)
"""


# give you explanation for the approach
def partition(arr, low, high):
    ptr = low
    pivot = arr[high]

    for i in range(low, high):
        if pivot >= arr[i]:
            # swap elements smaller than the pivot at the front
            arr[i], arr[ptr] = arr[ptr], arr[i]
            # increment position of pointer by 1
            ptr += 1
    # swap last elements with ptr
    arr[ptr], arr[high] = arr[high], arr[ptr]
    return ptr


# Function to do Quick sort 
def quickSort(arr, low, high):
    if len(arr) == 1: return arr

    if low < high:
        # partition function to swap elements around pivot
        pi = partition(arr, low, high)

        # sort left elements
        quickSort(arr, low, pi - 1)

        # sort right elements
        quickSort(arr, pi + 1, high)

    return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
