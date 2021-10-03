# Time Complexity : O(N log(N))
# Space Complexity : O(log(N))

# Exercise 2 : Quick Sort
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #setting pivot to low pointer initially
    pivot_index = low
    pivot = arr[pivot_index]

    #base condition, perform loop while low<high, when low overtakes high we will escape while loop and swap high and pivot element
    while low < high:
        # perform check while low does not exceed length of array and till we find element that is greater than pivot
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        #perform check till we find element that is lower than pivot
        while arr[high] > pivot:
            high -= 1
        #if the low pointer overtakes high the last time, we will stop decrementing or incrementing, and swap both elements respectively
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    #once low overtakes high, we will swap the pivot element with high, and now we have pivot element sorted
    arr[high],arr[pivot_index] = arr[pivot_index], arr[high]
    #we simply return the value of the high element that we swapped, so we can proceed to partition
    return high
  

# Function to do Quick sort 
def quickSort(arr,low,high): 

    if(low < high):
        #this will give us partition element, which is already sorted, we have to sort the division before and after this element
        p = partition(arr, low, high)

        #run quicksort recursively on the before and after sorted division respectively
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
