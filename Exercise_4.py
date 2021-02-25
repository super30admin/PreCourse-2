# Python program for implementation of MergeSort
def mergeSort(arr):

    #write your code here
    if not arr:
        return None

    def helper(head, tail):
        if head >= tail:
            return
        left, right = head, tail
        mid = left + (right - left) // 2
        pivot = arr[mid]
        while left <= right:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        helper(head, right)
        helper(left, tail)

    helper(0, len(arr) - 1)
    return arr


# Code to print the list
def printList(arr):

    #write your code here
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
