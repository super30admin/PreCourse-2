# Time Complexity: O(n lgn)
# Space Complexity: O(1) extra space

# Python program for implementation of MergeSort

def mergeSort(arr):
    mergeSortH(arr, 0, len(arr)-1)


def mergeSortH(arr, l, r):

    if l < r:

        m = l + (r - l) // 2

        mergeSortH(arr, l, m)
        mergeSortH(arr, m + 1, r)

        merge(arr, l, m, r)

def merge(arr, l, m, r):

    l2 = m + 1

    if arr[m] <= arr[l2]:
        return

    while l <= m and l2 <= r:

        if arr[l] <= arr[l2]:
            l += 1

        else:
            value = arr[l2]
            index = l2

            while index != l:
                arr[index] = arr[index - 1]
                index -= 1
            arr[l] = value

            l += 1
            m += 1
            l2 += 1


# Code to print the list 
def printList(arr):
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
