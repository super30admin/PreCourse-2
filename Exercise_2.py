"""
Problem - Implement Quick Sort recursively
Example - Input - numbers = [10,7,8,9,1,5]
          Output - [1,5,7,8,9,10]
Solution - Quick sort algorithm recursively. Use partition function with last element as pivot
Time Complexity - Worst case O(n^2), if we keep picking worst possible pivot for each iteration. very rare case.
                  Average case O(n log n), where n is number of elements in the given array
Space Complexity - O(1) , in place sorting
Test Cases - Edge Cases - Empty array, duplicates
             Base Cases - Array with 1 element, sorted input array
             Regular Cases - unsorted array with many elements
"""


# Function to find partition index
def partition(arr, low, high):
    i = low-1 # index of smaller element
    pivot = arr[high] # last element as pivot

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:
        return arr
    if low < high:
        # Make a partitioning index and put arr[pi] at the right place
        pi = partition(arr, low, high)
        # Sort elements before and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Driver code
mylist = [10, 7, 8, 9, 1, 5]
n = len(mylist)
print ("Given array is", mylist)
quickSort(mylist,0,n-1)
print("Sorted array is: ", mylist)

 
