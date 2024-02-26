# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Best case time complexity is O(NLogN) space complexity is O(1)
def partition(arr,low,high):
    # select pivot as highest element
    pi = arr[high]
    # assign lower value index
    i = low-1
    for j in range(low, high):
        # if the element is smaller than the pivot swap with the greater element pointed by i
        if arr[j] <= pi:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]   
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1            

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
