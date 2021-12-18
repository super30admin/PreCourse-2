# Python program for implementation of MergeSort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes


# recursively split array at the middle creating copies of each half
# sort sublists and merge them into the array
def mergesort(arr):
    if len(arr) <= 1:
        return

    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]

    mergesort(l)
    mergesort(r)

    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1


# Code to print the list
def printlist(arr):
    print(" ".join([str(x) for x in arr]))


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printlist(arr)
    mergesort(arr)
    print("Sorted array is: ", end="\n")
    printlist(arr)
