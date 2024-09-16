# Python program for implementation of Quicksort Sort 
# give you explanation for the approach

# Worst case time complexity: O(n^2); Average Case: O(n*log n)
# Space Complexity: O(1)


def partition(arr,low,high):
    # write your code here

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1
            # Swap
            arr[j], arr[i] = arr[i], arr[j]

    # Get i+1th position for the pivot
    arr[i+1], arr[high] = arr[high], arr[i+1]                  
    return i+1


# Function to do Quick sort
def quickSort(arr,low,high):    
    # write your code here
    if not arr: return
    if len(arr) == 1: return arr

    if low < high:
        
        pos = partition(arr, low, high)
        quickSort(arr, low, pos - 1)
        quickSort(arr, pos + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
