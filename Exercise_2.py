# Python program for implementation of Quicksort Sort

# Time: O(N log N) (avg case), O(N**2) (worst case)
# Space: O(log N) (avg case), O(N) (worst case)

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    i = low-1
    pivot = arr[high]
    # Rearrange elements such that
    # if ele <= pivot, then place ele to the left of pivot
    # if ele > pivot, then place ele to the right of pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 # next index to store the small element A[j]
            swap(arr, i, j)

    i += 1 # next index to store the pivot
    # At this point, swap the pivot element with
    # A[i]. Here, i = position of the pivot element
    # in the sorted array. i splits the array into
    # two parts, left subarray and right subarray
    # elements of left subarray <= pivot
    # elements of right arr > pivot.
    # But elements in left arr and right arr are not sorted.
    swap(arr, i, high)
    return i

# Function to do Quick sort
def quickSort(arr,low,high):
    #write your code here
    if len(arr) == 1:
        return arr[0]
    if low < high: # meaning at least two elements in array
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index-1)
        quickSort(arr, pivot_index+1, high)
    #print(f"sorted array = {arr}")
    return arr



# Driver code to test above
arr = [10, 7, 8, 9, 1, 5] # ans: [1, 5, 7, 8, 9, 10]
# arr = [7, 6, 10, 5, 9, 2, 1, 15, 7] # ans: [1,2,5,6,7,7,9,10,15]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
