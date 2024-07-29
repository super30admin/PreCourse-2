def mergeSort(arr):
    """
    Function to perform MergeSort on the array.
    
    :param arr: List[int], the array to be sorted
    """
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        mergeSort(left_half)
        mergeSort(right_half)

        # Initialize pointers for left, right, and main array
        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def printList(arr):
    """
    Function to print the elements of the list.
    
    :param arr: List[int], the list to be printed
    """
    for i in arr:
        print(i, end=" ")
    print()

# Driver code to test the above functions
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is:", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is:", end="\n")
    printList(arr)