# Python program for implementation of MergeSort 
def mergeSort(arr):
    # write your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        right = arr[mid:]
        left = arr[:mid]

        # Call merge sort on left (recursive)
        mergeSort(left)

        # Call merge sort on right (recursive)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        # Creating merged array from two halves
        while j < len(right) and i < len(left):
            if right[j] > left[i]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1


# Code to print the list 
def printList(arr):
    # write your code here
    for ele in arr:
        print(ele, end=" ")


# driver code to test the above code 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is:", end="\n")
    printList(arr)
    mergeSort(arr)
    print("\nSorted array is: ", end="\n")
    printList(arr)
