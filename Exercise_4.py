"""
Problem - Implement Merge Sort
Example - Input - mylist = [10,7,8,9,1,5]
          Output - [1,5,7,8,9,10]
Solution - Merge sort algorithm with recursive approach.
Time Complexity - O(n long n), where n is the number of elements in the list.
                  The list splits in log n time and it takes a linear time to merge it back
Space Complexity - O(n)
Test Cases - Edge Cases - Empty array, Null array, duplicates
             Base Cases - Array with 1 element, sorted input array
             Regular Cases - unsorted array with many elements
"""


# Recursive approach for Merge Sort
def merge_sort(mylist):
    if mylist is None or len(mylist) <= 1:
        return mylist

    mid = len(mylist) // 2
    left = mylist[:mid]
    right = mylist[mid:]

    # Recursive call on left and right half
    merge_sort(left)
    merge_sort(right)

    # two iterators for traversing the two halves
    i = j = 0

    # iterator for the main list
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            # use value from the left half
            mylist[k] = left[i]
            i += 1
        else:
            mylist[k] = right[j]
            j += 1
        # move to the next slot
        k += 1

    # For all the remaining values
    while i < len(left):
        mylist[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        mylist[k] = right[j]
        j += 1
        k += 1


# Driver code
mylist = [12, 11, 13, 5, 6, 7]
print ("Given array is", mylist)
merge_sort(mylist)
print("Sorted array is: ", mylist)

