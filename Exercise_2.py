# Time complexity: O(nlog(n)) ; n = no. of elements
# Space complexity: O(n) 

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Take last element as pivot. Initialize i as low - 1
# Now until j reaches high, do -> if arr[j]<pivot, increment i and swap arr[i] and arr[j]
# Atlast swap arr[i+1] with arr[high], and we got an element at its correct index, which will be the partition index, return that index, and this whole process will be 
# repeated until array is sorted.
def partition(arr,low,high):
  #write your code here
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        part_elem_idx = partition(arr, low, high)
        quickSort(arr, low, part_elem_idx-1)
        quickSort(arr, part_elem_idx+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
