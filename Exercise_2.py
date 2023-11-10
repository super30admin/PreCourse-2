# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# The approach: Finding out pivot (last element taken). Comparing the value of pivot with other elements.
                # If the array element is larger than the pivot, do nothing. Assign a pointer for indicating the
                # index of smaller elements (used for swapping with larger elements).
                # If the element is smaller than the pivot, swap that element with the larger element found before
                # using the above pointer. Return the partition index and recursively call the quickSort function.

#Time complexity for:
    # partition of elements = n
    # quicksort = O(nlogn)

# Space complexity for quicksort = O(n)

def partition(arr,low,high):
  
  
    #write your code here

    pivot = arr[high]  # Taking the pivot as the last element of the array
    ip = low - 1  # This pointer indicates the index of smaller element
    for j in range(low, high):
        if arr[j] < pivot:
            ip += 1
            arr[j], arr[ip] = arr[ip], arr[j]
    arr[ip + 1], arr[high] = arr[high], arr[ip + 1]
    return ip + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here

    if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
