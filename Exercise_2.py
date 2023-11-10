# Time Complexity: O(N^2) worst case for already sorted, O(NlogN) average
# Space Complexity: O(N) worst case, O(logN) average

# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr,low,high):

    pivot = arr[high]
    i = low - 1

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)


# Function to do Quick sort
def quickSort(arr,low,high):

    #write your code here
    if (low < high):
        sorted_elem:int = partition(arr,low,high)
        quickSort(arr,low,sorted_elem-1)
        quickSort(arr,sorted_elem+1,high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5, 2, 0, 11, 3, -5, 10]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("{}".format(arr[i]), end=" ")