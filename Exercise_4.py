# Python program for implementation of MergeSort

def helper(arr1, arr2):
    ans = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            ans.append(arr2[j])
            j += 1

    if i < len(arr1):
        while i < len(arr1):
            ans.append(arr1[i])
            i += 1

    if j < len(arr2):
        while j < len(arr2):
            ans.append(arr2[j])
            j += 1

    return ans


def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    arr1 = mergeSort(arr[:mid])
    arr2 = mergeSort(arr[mid:])
    return helper(arr1, arr2)


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])


# driver code to test the above code 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    sorted_arr = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(sorted_arr)
