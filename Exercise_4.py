# Time Complexity = O(nLogn)  Space Complexity = O(n)


# Python program for implementation of MergeSort
def mergeSort(arr, l, r):
    if l < r:
        mid = (l + r) // 2  # find the mid of array
        mergeSort(arr, l, mid)  # pass the left part of array to mergesort
        mergeSort(arr, mid + 1, r)  # pass the right part of array to mergesort
        merge(arr, l, mid, r)  # Merge all divided array


def merge(arr, l, mid, r):
    n1 = mid - l + 1  # Initialize the size of Left array
    n2 = r - mid  # Initialize the size of Right array
    lArr = []
    rArr = []
    for i in range(0, n1):  # Construct left array which is the left hand side of mid
        lArr.append(arr[l + i])
    for i in range(0, n2):
        rArr.append(
            arr[mid + 1 + i]
        )  # Construct right array which is the right hand side of mid

    # Initialize pointers to traverse from left , right, and main array correspondingly
    # here k starts from l location as we have to store element in the main array from start location which is  l for each case

    i, j, k = (0, 0, l)
    # compare element from left array and right array and store it in the main array accordingly
    while (i < n1) and (j < n2):
        if lArr[i] <= rArr[j]:
            arr[k] = lArr[i]
            i += 1
            k += 1
        else:
            arr[k] = rArr[j]
            j += 1
            k += 1

    # Store remaining elements after comparison in the main array
    while i < n1:
        arr[k] = lArr[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = rArr[j]
        j += 1
        k += 1


# Code to print the list
def printList(arr):
    print(arr)


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array is: ", end="\n")
    printList(arr)
