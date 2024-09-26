'''
Merge Sort: Out-of-place sorting algorithm

Time Complexity:
merge_sorted_arrays(): O(2n) where n is the length of max(arr_a, arr_b)
mergeSort(): Halve the array into two halves and call merge_sorted_arrays() for both halves,
             This halving operation thus happens logn times. O(logn * 2n) ~ O(logn * n)

Space Complexity:
merge_sorted_arrays(): O(2n) ~ O(n) where n is the length of max(arr_a, arr_b)
mergeSort(): O(logn * 2n) ~ O(logn * n) where n is the length of max(arr_a, arr_b) since mergeSort() calls merge_sorted_arrays() logn times and at each call, there are
             2n auxiliary locations created.

Issue while implmenting: No

'''


def merge_sorted_arrays(arr_a,arr_b):

    # create an auxiliary array
    arr_c = []

    arr_a_pointer = 0
    arr_b_pointer = 0

    for idx in range(len(arr_a) + len(arr_b)):

        if arr_a_pointer <= len(arr_a)-1 and arr_b_pointer <= len(arr_b)-1:
            # If both arr_a and arr_b have elements left, appent the lowest of the two
            if arr_a[arr_a_pointer] < arr_b[arr_b_pointer]:
                arr_c.append(arr_a[arr_a_pointer])
                arr_a_pointer += 1
            else:
                arr_c.append(arr_b[arr_b_pointer])
                arr_b_pointer += 1
        elif arr_a_pointer > len(arr_a)-1:
            # If no element left in arr_a
            arr_c.extend(arr_b[arr_b_pointer:])
            return arr_c
        else:
            # If no element left in arr_b
            arr_c.extend(arr_a[arr_a_pointer:])
            return arr_c








def mergeSort(arr):

    # Base case for divide-and-conquer
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        left_half = arr[0:mid]
        right_half = arr[mid:len(arr)]

        # Recursively sort each half
        sorted_left_half = mergeSort(left_half)
        sorted_right_half = mergeSort(right_half)

        # Merge the sorted halves and return the final array
        return merge_sorted_arrays(sorted_left_half, sorted_right_half)






# write your code here

# Code to print the list
def printList(arr):
    print(arr)


# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    arr = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
