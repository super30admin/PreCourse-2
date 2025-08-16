# Python program for implementation of Quicksort Sort 
#Time Complexity: O(n log n)
#Space Complexity: O(n log n)
# give you explanation for the approach

"""QuickSort is a divide-and-conquer sorting algorithm where we usually Choose a pivot element from the array.
Partition the array:

All elements smaller than the pivot go to the left.

All elements greater than the pivot go to the right.

Recursively apply the same steps to the left and right subarrays.
"""
def partition(arr,low,high):

#write your code here
    mid = (low + high) // 2
    pivot = arr[mid]  # Take middle element as pivot
    i = low -1 

    # Move pivot to end temporarily
    swap(arr, mid, high)

    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    # Move pivot to its final place
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    #Recursive quick sort
    if low < high:
        partition = partition(arr,low,high) 
        quickSort(arr, low, partition - 1)
        quickSort(arr, partition + 1, high)

if __name__ == "__main__":  
# Driver code to test above 
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr) 
    quickSort(arr,0,n-1) 
    print ("Sorted array is:") 
    for i in range(n): 
        print ("%d" %arr[i])
  
 
