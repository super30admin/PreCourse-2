# Python program for implementation of MergeSort 
# Time Complexity : 
#   Best / Average / Worst = O(n log n)
# Space Complexity : 
#   O(n) extra — due to creating temporary subarrays during merging (plus O(log n) recursion stack)
# Did this code successfully run on Leetcode : 
#   Yes, this standard top-down Merge Sort passes (e.g., for “Sort an Array”).
# Any problem you faced while coding this : 
#   - Remembering to copy any remaining elements from the left/right halves after the main merge loop.
#   - Python slicing creates extra arrays, so space is O(n). An index-based merge can reduce allocations.
#   - Deep recursion can be an issue for extremely large n (Python recursion limit).


def mergeSort(arr):
    """
    Top-down recursive Merge Sort.
    Splits the array, recursively sorts the halves, then merges them back.
    Time: O(n log n)
    Space: O(n) extra because of temporary arrays created during merge.
    """
    if len(arr) > 1:
        mid = len(arr) // 2           # Find the middle point
        L = arr[:mid]                 # Left half
        R = arr[mid:]                 # Right half

        # Recursively sort both halves
        mergeSort(L)
        mergeSort(R)

        # Merge the sorted halves back into arr
        i = j = k = 0

        # Merge while both halves have elements
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy any remaining elements of L (if any)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy any remaining elements of R (if any)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list 
def printList(arr):
    for x in arr:
        print(x, end=" ")
    print()


# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is")
    printList(arr) 
    
    mergeSort(arr) 
    
    print("Sorted array is:")
    printList(arr)
