# Python program for implementation of MergeSort

"""
Approach --
1. Find mid. Create temp left and temp right arrays to store left of mid and right of mid values
2. Compare left and right array values and combine & add them to the arr
3. Continue till the end of temp arrays left and right

Time complexity - O(nlogn)
Space complexity - O(n)
"""


def mergeSort(arr):
    if len(arr) > 1:
        # declare mid
        mid = len(arr) // 2

        # Create temp arrays with left and right values from mid-point
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # run mergesort
        mergeSort(left_arr)
        mergeSort(right_arr)

        # add values to arr by comparing left and right arrays
        i, j, k = 0, 0, 0

        while i < len(left_arr) and j < len(right_arr):
            # compare value in left and right array
            # add values in increasing order
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # check if any elements are remaining
        while i < len(left_arr):
            # add any remaining elements to arr
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # check if any elements are remaining
        while j < len(right_arr):
            # add any remaining elements to arr
            arr[k] = right_arr[j]
            j += 1
            k += 1


# Code to print the list 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])


# driver code to test the above code 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
