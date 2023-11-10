# Python program for implementation of Quicksort Sort 
  
#TimeComplexity: O(n log n)
#SpaceComplexity: O(n)
def partition(arr,low,high):
  
    #set last element as pivot
    pivot = arr[high]
    #keep track of the index of swaps when the element is smaller than pivot element
    small_iter = low-1
    
    #for all element before pivot element
    for i in range(low, high):
        #if the element is smaller take it to the front of array else do nothing
        if arr[i]<pivot:
            small_iter += 1
            arr[small_iter], arr[i] = arr[i], arr[small_iter]
    #place the pivot element just after the element swapped as they are smaller
    #we obtain correct index for pivot element
    arr[small_iter + 1], arr[high] = arr[high], arr[small_iter + 1]
    
    #return the partition index where we placed the pivot element
    return small_iter+1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #if there are more than one elements in the arr
    if low<high:
        #obtain the partition index
        partition_index = partition(arr, low, high)
        
        #perform quick sort for elements before and after partition
        quickSort(arr, low, partition_index-1)
        quickSort(arr, partition_index+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
