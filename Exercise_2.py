# Python program for implementation of Quicksort Sort 
#  Time Complexity: nlog(n)
#  Space Complexity: O(1)
# give you explanation for the approach
# 1. Take first element as the pivot element.
# 2. Increment the low pointer until while traversing you find an element greater than pivot.
# 3. Decrement the high pointer until while traversing you find an element smaller than pivot.
# 4. If low and high elements don't cross each other, then swap both.
# 5. If low and high elements cross each other, swap high element with pivot and return high index.

def partition(arr,low,high):

    index = low
    pivot = arr[index]

    while low < high:

        while low < len(arr) and arr[low] <= pivot:
            low += 1
    
        while arr[high] > pivot:
            high -= 1

        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    arr[index], arr[high] = arr[high], arr[index]

    return high

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end = " "), 
  
 
