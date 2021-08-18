# Time Complexity : O(N)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Couldn't find on Leetcode
# Any problem you faced while coding this : None
# Python program for implementation of MergeSort
"""
Merge sort:
Split array in half
call merge sort on each half to sort them recursively
merge both sorted halves into one sorted array
"""


def mergeSort(arr):
    if len(arr) > 1:
        left_sub_arr = arr[:len(arr) // 2]
        right_sub_arr = arr[len(arr) // 2:]

        # recursion
        mergeSort(left_sub_arr)
        mergeSort(right_sub_arr)

        # merge
        l = 0  # left arr idx
        r = 0  # right arr idx
        i = 0  # arr idx
        while l < len(left_sub_arr) and r < len(right_sub_arr):
            if left_sub_arr[l] < right_sub_arr[r]:
                arr[i] = left_sub_arr[l]
                l += 1
            else:
                arr[i] = right_sub_arr[r]
                r += 1
            i += 1
        # for remaining array
        while l < len(left_sub_arr):
            arr[i] = left_sub_arr[l]
            l += 1
            i += 1
        while r < len(right_sub_arr):
            arr[i] = right_sub_arr[r]
            r += 1
            i += 1


# write your code here

# Code to print the list
def printList(arr):
    print(*arr)


# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is: ", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
