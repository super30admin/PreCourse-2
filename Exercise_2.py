# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# quicksort is a recursive function. Each iteration you find pivot using partition - pivot is that element in the array
# where all elements to left of it is less than pivot and all elements to right of it is greater than pivot.
# Then, we recursively call quicksort on both the halves.
def partition(arr,low,high):
    greater_ind = low
    pivot = arr[high]
    for curr_ind in range(low, high):
        if arr[curr_ind] < pivot:
            arr[curr_ind], arr[greater_ind] = arr[greater_ind], arr[curr_ind]
            greater_ind += 1
    arr[greater_ind], arr[high] = arr[high], arr[greater_ind]
    return greater_ind

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pivot_ind = partition(arr, low, high)
        quickSort(arr, low, pivot_ind - 1)
        quickSort(arr, pivot_ind + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
