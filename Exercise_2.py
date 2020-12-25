# Python program for implementation of Quicksort Sort

# give you explanation for the approach
'''
Uses Divide-and-Conquer approach. Runs in O(n*log(n)).
1. Selects a pivot element (usually the last element of the list).
2. Then, traverses the sub array and arranges elements such that all the elements less than pivot are separated from all the elements greater than pivot.
3. And then performs the same operation recursively on the left and right subarrays.
'''
def partition(arr, low, high):
    #write your code here
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# Function to do Quick sort
def quickSort(arr, low, high):
    #write your code here
    if low >= high:
        return

    pi = partition(arr, low, high)
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
