# Time Complexity:
#   Best Case: O(n log n) - Every split and merge takes log(n) depth levels.
#   Average Case: O(n log n) - Same as the best case.
#   Worst Case: O(n log n) - Even for the worst input, the algorithm performs consistently.

# Space Complexity: O(n) - Temporary arrays are used for merging.

# Did this code successfully run on Leetcode?
# Yes, it works for typical sorting problems.

# Any problem you faced while coding this:
# Handling large input sizes can lead to increased memory usage, but it works efficiently.

# Your code here along with comments explaining your approach:
# - Merge Sort is a **divide-and-conquer** algorithm.
# - We repeatedly split the array into halves until we get single-element arrays.
# - Then we **merge** the sorted halves back together in the correct order.

def mergeSort(arr):
    """
    Recursively split the array and merge the sorted halves.
    """
    if len(arr) > 1:
        # Find the middle point
        mid = len(arr) // 2

        # Divide the array elements into two halves
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        # Recursively sort both halves
        mergeSort(L)
        mergeSort(R)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to the original array while comparing elements from L and R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check for any remaining elements in L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Check for any remaining elements in R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    """
    Function to print the array elements.
    """
    for i in arr:
        print(i, end=" ")
    print()

# Driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)