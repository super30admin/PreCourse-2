# Python program for implementation of MergeSort
def mergeSort(arr):
    def helper(low, high):
        if low == high:
            return arr[low:high+1]
        if low > high:
            return []
        mid = low + (high - low) // 2
        left = helper(low, mid)
        right = helper(mid + 1, high)
        return merge(left, right)
    return helper(0, len(arr) - 1)


def merge(arr1, arr2):
    i, j = 0, 0
    l1, l2 = len(arr1), len(arr2)
    arr = []
    while i < l1 and j < l2:
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    arr += arr1[i:]
    arr += arr2[j:]
    return arr


# Code to print the list
def printList(arr):
    print(",".join(map(str, arr)))


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    arr = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
