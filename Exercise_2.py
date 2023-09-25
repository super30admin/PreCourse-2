# Python program for implementation of Quicksort Sort 

def partition(arr,low,high):
    # chose the rightmost element as pivot
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment pointer for greater element
            i += 1
            # Swap the elements
            arr[i], arr[j] = arr[j] , arr[i]
    # swap the pivot element with the greater element pointed to by i
    arr[i+1], arr[high] = arr[high], arr[i+1]

    # return the position of the pivot
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pi = partition(arr, low, high)
        
        # recursive call on left of pivot
        quickSort(arr, low, pi-1)
        
        # recursive call on right of pivot
        quickSort(arr, pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d" %arr[i])
