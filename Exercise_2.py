# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Ys
# Any problem you faced while coding this : No
# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    # assigning an last element from the list as pivot element
    pivotElement = arr[high]
    # assigned the greatest element
    value = (low-1)
    # checking each element from the list with the pivot
    for j in range(low, high):
        # checking if the element is <= pivot element, if satisfies swap it with larger element
        if arr[j] <= pivotElement:
            value += 1
            # swap the taken element with the element of index j
            temp = arr[j]
            arr[j] = arr[value]
            arr[value] = temp
    # swap the pivot element with the larger element specified by value
    temp = arr[high]
    arr[high] = arr[value+1]
    arr[value+1] = temp
    return (value+1)


def quickSort(arr, low, high):
    # checking the pivot element, if value is less than pivit element are placed to the left of the pivot       #and greater placed on the right.
    if(low < high):
        # when the value is at right place
        p = partition(arr, low, high)
        # sorting elements, before and after partition
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)


# Driver code to test above
arr = [0, 7, 6, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
