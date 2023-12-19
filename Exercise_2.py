# Python program for implementation of Quicksort Sort 
## Time complexity : Best O(n logn) and Worst O(n^2)
## Space complexity : O(n)

# give you explanation for the approach
def partition(arr,low,high):
  
    #Chossing the rightmost element as pivot
    pivot = arr[high]
    i = low - 1

    #Traverse through all elements and swapping based on pivot
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i] , arr[j] = arr[j], arr[i]

    #Swapping the pivot element with the greatest element
    arr[i+1], arr[high] = arr[high], arr[i+1]

    #Return the position from where the partition is done
    return i+1
 
# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here

    if low < high:

        #Finding pivot index and making recursive calls to divide the array based on pivot

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
  
 
