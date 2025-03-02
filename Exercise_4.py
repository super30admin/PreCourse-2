# Python program for implementation of MergeSort
# Divide-and-conquear algorithm in which array gets splitted recursively
# until left with one element and then gets merged back in sorted array

# Time complexity: O(nlog n) as array is splitting in two halves and each half is processed seperately
# Space Complexity: O(n) as temp arrays are getting used


def mergeSort(arr):

    # write your code here
    if len(arr) > 1:  # if only one element, already sorted
        mid = len(arr) // 2  # get the mid

        leftHalf = arr[:mid]  # left subarray
        rightHalf = arr[mid:]  # right subarray

        # recursion to split both the sides
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        # merge back together in sorted manner
        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        # if element left in leftHalf
        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1
        # if any element left in right Half
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):

    # write your code here
    for i in arr:
        print(i, end="\n")


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
