# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

def swap(arr, a, b):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
def partition(arr, low, high):
    pivot_index = low
    pivot = arr[pivot_index]

    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1

        if low < high:
            swap(arr, low, high)

    swap(arr, pivot_index, high)

    return high
#using the Hoare approach, choosing low as pivot and comparing low with pivot
#till it's greater than pivot and comparing high with pivot till it's less than pivot
#swaping low and high again repeating the process till low and crosses each other
#swaping high with pivot then taking care of left and right side arr of pivot again with above logic

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
