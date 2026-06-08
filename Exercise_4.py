# Time Complexity : O(n log n):array is split log n times, each level takes O(n) to merge
# Space Complexity : O(n): extra space used for L and R arrays at each split
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Approach: divide the array in half recursively until single elements,then merge two sorted halves back by always picking the smaller element first

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:                      # base case: stop if single element

        mid = len(arr) // 2               # find the middle index

        L = arr[:mid]                     # left half
        R = arr[mid:]                     # right half

        mergeSort(L)                      # recursively sort left half
        mergeSort(R)                      # recursively sort right half

        i = j = k = 0                    # i → left pointer, j → right pointer, k → arr pointer

        while i < len(L) and j < len(R): # compare elements from both halves
            if L[i] <= R[j]:             # left element is smaller or equal
                arr[k] = L[i]            # place left element into arr
                i += 1                   # move left pointer forward
            else:                        # right element is smaller
                arr[k] = R[j]            # place right element into arr
                j += 1                   # move right pointer forward
            k += 1                       # move arr pointer forward

        while i < len(L):               # copy remaining left elements if any
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):              # copy remaining right elements if any
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")         # print each element separated by space
    print()                            # move to next line after all elements

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)