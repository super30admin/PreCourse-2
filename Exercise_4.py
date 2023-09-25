# Python program for implementation of MergeSort

# Time Complexity : O(n log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : no
# Any problem you faced while coding this : Facing problem in understanding how to store the result in the given
# array instead of creating a new list


def mergeSort(arr):
    # if only one element in the array, return the array since its already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # split arr in two halves and keep doing it until you get an array of single element (i.e. meaning its sorted)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    # pass sorted arrays to merge function to merge them
    return (merge(left, right))


def merge(arr_1, arr_2):
    sorted_list = []
    i = j = 0

    # iterate through each element in both the arrays until either of them runs out
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            sorted_list.append(arr_1[i])
            i += 1
        else:
            sorted_list.append(arr_2[j])
            j += 1

    # if array 2 ran out, append whatever outstanding in array 1 as it is to the sorted list
    while i < len(arr_1):
        sorted_list.append(arr_1[i])
        i += 1

    # if array 1 ran out, append whatever outstanding in array 2 as it is to the sorted list
    while j < len(arr_2):
        sorted_list.append(arr_2[j])
        j += 1

    return sorted_list


# write your code here

# # Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")


# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 3, 100]
    print("Given array is", end="\n")
    printList(arr)
    out = mergeSort(arr)
    print("\nSorted array is: ", end="\n")
    # print (out)
    printList(out)
