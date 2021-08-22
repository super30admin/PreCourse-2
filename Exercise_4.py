# time complexity: O(nlogn)
# space complexity: O(1)
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i+= 1
                k += 1
            else:
                arr[k] = right_half[j]
                j+= 1
                k+= 1

        while i < len(left_half):
            arr[k] = left_half[i]
            k+=1
            i +=1
        while j < len(right_half):
            arr[k] = right_half[j]
            k+=1
            j +=1


# Code to print the list
def printList(arr):
    print(arr)

# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
