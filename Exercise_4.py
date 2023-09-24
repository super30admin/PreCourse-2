#Time Complexity O(nlogn)
#space Complexity O(n)


# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        L = arr[:mid]  # Split the array into two halves
        R = arr[mid:]

        mergeSort(L)  # Recursively sort the first half
        mergeSort(R)  # Recursively sort the second half

        i = j = k = 0

        # Copy data to temporary lists L and R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])
    print()

# Driver code to test the MergeSort implementation
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is:")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is:")
    printList(arr)




