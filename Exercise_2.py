# Python program for implementation of Quicksort Sort 
# Time complexity - O(n^2) (Worst case)   O(nlogn) - Average scenario
# Space complexity - O(1)

# The pivot is used as the last element and the pointer as the first element from the list. The pointer will keep track of the numbers that are smaller than the pivot. 
# In this solution, x is the pointer
# If any values are smaller than the pivot, then those will be swapped. Then, we will swap the last number with the pointer(x) and return it.
# Now the element at pivot position is at its correct sorted position in the array and its index is called as pi(partition index)
# pi divides the array into 2 unsorted arrays to its left and right
# now simply apply quicksort to the elements left to pi and then to the right of pi

def partition(arr, low, high):    
    pivot = arr[high]
    x = low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[x] = arr[x], arr[i]
            x = x+1
    arr[x], arr[high] = arr[high], arr[x]
    return x

# Function to do Quick sort 
def quickSort(arr, low, high):              # Partition is not needed if low >= high    
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr, 0, n-1) 
print ("Sorted array is:") 
for i in range(n):
    print (arr[i], end=" ")

 