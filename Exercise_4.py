# Python program for implementation of MergeSort
#Time complexity: O(nlogn) Diving array into halves takes logn and merging is O(n)
#Sapce complexity: O(n) for string intermediate arrays
def mergeSort(arr):
    def _mergeSort(arr, s, e):
        # write your code here
        if e - s + 1 <= 1:
            return
        m = (s + e) // 2
        _mergeSort(arr, s, m)
        _mergeSort(arr, m + 1, e)
        merge(arr, s, m, e)

    _mergeSort(arr, 0, len(arr) - 1)


def merge(arr, s, m, e):
    Left = arr[s : m + 1]
    Right = arr[m + 1 : e + 1]
    i = 0
    j = 0
    k = s
    while i < len(Left) and j < len(Right):
        if Left[i] <= Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1
    while i < len(Left):
        arr[k] = Left[i]
        k += 1
        i += 1
    while j < len(Right):
        arr[k] = Right[j]
        k += 1
        j += 1


# Code to print the list
def printList(arr):
    # write your code here
    for a in arr:
        print(a)


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
