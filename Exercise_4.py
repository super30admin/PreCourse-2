# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        # Slicing array
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        # initialising l,r,i
        l = 0
        r = 0
        i = 0  # for merged array

        # Take the smallest from left and right, add to the merged array
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1

        # Copying remaining elements
        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1

# Code to print the list
def printList(arr):
    for i in arr:
        print(str(i) + " ")


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
