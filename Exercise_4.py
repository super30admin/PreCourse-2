# Python program for implementation of MergeSort 
def mergeSort(arr):
    '''
    Time Complexity: O(n log n )
    Space Complexity: O(n)
    '''

    # make sure to add a base case for recursion
    if len(arr) > 1:
        # find the middle of the array
        mid = len(arr) // 2

        # divide the array into 2 so you can divide and conquer
        left = arr[:mid]
        right = arr[mid:]

        # sort both recursivley
        mergeSort(left)
        mergeSort(right)

        # you will need 3 iterators.  2 for the first two halves, 1 for the whole list
        i = 0 # for left
        j = 0 # for right
        k = 0 # for main list

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # here we can see that the left is smaller, so swap in main arr
                arr[k] = left[i]
                i += 1
            else:
                # otherwise right is smaller so swap
                arr[k] = right[j]
                i += 1
            k += 1

        # the while loops cleanup partially completed temp arrays
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
