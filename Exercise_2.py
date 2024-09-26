'''
Recursive Quick Sort: In-place sorting

Time Complexity:
    partition(): O(n)
    quickSort(): Since at each level, we do n comparisions inside the partition() function
                and in the worst case you divide the array into 1 and ( len(array) - 1 elements), TC becomes O(n^2)

Space Complexity: O(1) for both methods since the size of the auxiliary space doesnt vary with the size of the input.

Issue while implementing: No
'''

# This function is same in both iterative and recursive implementations of quicksort.
def partition(arr, low, high):
    '''
    :param arr: an array which needs to be sorted using quicksort
    :param low: the lowest index value of the passed array arr in terms of the original array indexing
    :param high: the highest index value of the passed array arr in terms of the original array indexing
    :return: an index position for the pivot element that separates arr into two halves while placing the pivot element in its sorted position
    '''


    pivot = arr[high]

    index_to_store_elem_less_than_pivot = low

    for idx in range(low, high):
        if arr[idx] < pivot:
            arr[index_to_store_elem_less_than_pivot], arr[idx] = arr[idx], arr[index_to_store_elem_less_than_pivot]

            #Now that this element has been placed before the pivot, we need to move to the next position
            index_to_store_elem_less_than_pivot += 1

    # Put the pivot element that is at the end of the array to its correct sorted position
    arr[high], arr[index_to_store_elem_less_than_pivot] = arr[index_to_store_elem_less_than_pivot], arr[high]

    # return this position that contains the sorted element, now we can sort the two halves of the array independently
    return index_to_store_elem_less_than_pivot


# write your code here


# Function to do Quick sort 
def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high) # find the correct location of the pivot element
        quickSort(arr, low, pivot-1) # in-place sort the left half
        quickSort(arr, pivot+1, high) # in-place sort the right half





# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
