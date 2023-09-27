# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1 # Pointer fixed at the beginning of the array
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pi = partition(arr, low, high)
        # recursive call on the left of pivot
        quickSort(arr, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(arr, pi + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
