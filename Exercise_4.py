# Python program for implementation of MergeSort
"""
Rasika Sasturkar
Time complexity: O(nlogn)
Space complexity: O(n)
"""


def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        l_list = arr[:m]
        r_list = arr[m:]

        # sort the halves individually
        mergeSort(l_list)
        mergeSort(r_list)

        # merge the 2 lists
        i, j, k = 0, 0, 0
        while i < len(l_list) and j < len(r_list):
            if l_list[i] < r_list[j]:
                arr[k] = l_list[i]
                i += 1
            else:
                arr[k] = r_list[j]
                j += 1
            k += 1
        while i < len(l_list):
            arr[k] = l_list[i]
            i += 1
            k += 1
        while j < len(r_list):
            arr[k] = r_list[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in arr:
        print(i, end=" ")


# driver code to test the above code
def main():
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("\nSorted array is: ", end="\n")
    printList(arr)


if __name__ == '__main__':
    main()
