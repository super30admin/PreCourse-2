# Time complexity - O(n log n)
# Space complexity - O(n)
# Code runs properly

# Approach:
# Merge sort is divide and conquer algorithm.
# Array is recursively divided into two halves until subarrays has size of one.
# Then, during merge step, two sorted halves are combined into single sorted array.
# Continue until entire array is merged and sorted.

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in arr:
        print(i, end=" ")
    print()

if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is:")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is:")
    printList(arr)
