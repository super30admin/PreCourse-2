# Python program for implementation of Quicksort Sort 
# timecomplexity: O(logn), space complexity: O(1)
#No problems faced
# give you explanation for the approach
def partition(arr, low, high):
    #base conditions
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        #arrange the array according to finding the exact position of the pivotal element
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Function to do Quick sort 
def quickSort(arr, low, high):
    if low < high:
        #Find a pivot for making 2 partitions where one side is all the elements
        # that are lesser than the pivot and other side more than the pivot
        pi = partition(arr, low, high)
        #recursively sort the 2 partitions made by the pivot
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi, high)

    # write your code here


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
