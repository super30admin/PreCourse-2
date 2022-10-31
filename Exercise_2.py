# Python program for implementation of Quicksort Sort 
#Time Complexity Worst Case: O(n2), Average case : O(nlogn)
#Space Complexity: O(1)
# give you explanation for the approach
def partition(arr,low,high):
    #set pivot to the last element in arr
    pivot = arr[high]

    #set a pointer to track greater element
    i = low - 1
    
    # traverse all element and compare each with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # if element found is greater than the pivot swap 
            (arr[i], arr[j]) = (arr[j], arr[i])
            i = i + 1
       # Swap the pivot element with the greater element specified by i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
        # Return the position from where partition is done
    return i + 1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pi = partition(arr, low, high)
    # Recursive call on the left of pivot
        quickSort(arr, low, pi - 1)
    # Recursive call on the right of pivot
        quickSort(arr, pi + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
