# Python program for implementation of Quicksort Sort 
'''This function takes last element as pivot, places the pivot element at its correct
position in sorted array, and places all smaller (smaller than pivot) to left of
pivot and all greater elements to right of pivot'''

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element to correct position
  

    # Swap the pivot element with the element at i+1 so it's in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partition index

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code 
    if low < high:
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1) # before
        quickSort(arr, pi + 1, high) # after partition
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
