# Python program for implementation of MergeSort
def mergeSort(arr):
    # write your code here
    '''
    Divide the array into two halves,
    create 2 sub arrays of array using
    the midpoint. Recursively continue
    to do this for both left and right part
    of the array until single elements
    exist. Then check max of these elements
    and merge them back to the array.
    For eg. 3 1 5 2 -> left =  3 1 and
    right = 5 2 -> 1 3 | 2 5 -> 1 2 3 5
    Time Complexity: O(n logn)
    Space ComplexitY: O(n)
    '''
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1
            elif left[i] > right[j]:
                arr[k] = right[j]
                j = j + 1

            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            arr[k] = right[j]
            k = k + 1
            j = j + 1


# Code to print the list
def printList(arr):
    '''
    Iterate through list and print elements
    until end of list
    '''
    for element in arr:
        print(element)
    # write your code here


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
