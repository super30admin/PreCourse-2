# Python program for implementation of Quicksort Sort 

# Technically, quick sort follows the below steps:
# Step 1 − Make any element as pivot
# Step 2 − Partition the array on the basis of pivot
# Step 3 − Apply quick sort on left partition recursively
# Step 4 − Apply quick sort on right partition recursively
# give you explanation for the approach
def partition(arr,low,high, pivot):
    #write your code here
    
    while(low <= high):

        while(arr[low] < pivot):
            low += 1
        
        while(arr[high] > pivot):
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    return low
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    # TC O(nlogn) in best case, in worst case it can be O(n^2)
    # SC O(1) as we are doing all computations in place 
    # Note: we are using recursion and that causes Stack Space usage
    #write your code here
    if low >= high: # if indices cross, we terminate
        return
    pivot = arr[(low + high) // 2]  # pick middle-element as Pivot
    idx = partition(arr, low, high, pivot) # partition using pivot
    quickSort(arr, low, idx-1) # partition returns partition index and we use that
    quickSort(arr, idx, high) # to further run quick sort in recursion

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5 ,1, 5, 77, 33, 11, 878, 123 ] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
