# Python program for implementation of MergeSort

# Time complexity for merge sort is O(n log n) and space complexity is O(n)

# Explanation: With the mergeSortHelper() function, we divide the array into middle index with lower bound considered. First divide will at [12, 11, 13] followed by [12, 11] etc., 
# then as the base value is reached with middle value of 0, we enter the merge() function where we first evaluate if 12 < 11 (j & k), since it is not, we set the arr[0] element as 11, 
# then we move the right side k pointer to increment along with array pointer i and then in the next while loop, the j pointer value is set to the next i pointer i.e. i[1] = 12 giving [11, 12]. 
# Then, on next occasion, with middle value 1, [12, 11] and [13] gets evaluated and set in order. Once the left side is evaluated, similar process follows for right side array [5, 6, 7]. 
# Then at main level with array as [11, 12, 13, 5, 6, 7], both the right and left side merge will take place and post comparison we get final result [5, 6, 7, 11, 12, 13].

def mergeSort(arr):
    def merge(arr, left, mid, right):
        left_side, right_side = arr[left:mid + 1], arr[mid + 1:right + 1]  # Splitting the left and right halves of the array.
        i, j, k = left, 0, 0                                               # i pointer is for the main array. j & k are pointers in sub-arrays.

        while j < len(left_side) and k < len(right_side):
            if left_side[j] <= right_side[k]:
                arr[i] = left_side[j]
                j += 1
            else:
                arr[i] = right_side[k]
                k += 1
            i += 1

        # Only one of the two below while loops will be run in the function.
        while j < len(left_side):
            arr[i] = left_side[j]
            j += 1
            i += 1

        while k < len(right_side):
            arr[i] = right_side[k]
            k += 1
            i += 1

    def mergeSortHelper(start, end):                                      # Defining start and end pointers to determine the portion of subarray we are running merge sort on.
        if start == end:
            return arr

        middle = (start + end) // 2

        mergeSortHelper(start, middle)
        mergeSortHelper(middle + 1, end)

        merge(arr, start, middle, end)
        return arr

    return mergeSortHelper(0, len(arr) - 1)                               # Initial start pointer to be set to 0 and end pointer is length of passed array minus 1.


# Code to print the list
def printList(arr):
    if len(arr) > 1:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)