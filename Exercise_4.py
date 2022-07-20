def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge_two_sorted(left, right)


def merge_two_sorted(arr1, arr2):
    i = 0
    j = 0
    sorted_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is: ", end="")
    print(arr)

    print("Sorted array is: ", end="")
    print(mergeSort(arr))
