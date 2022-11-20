#Time complexity: O(nlogn)
#Space complexity: O(logn)

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[high] #consider the last element as pivot
    i = low-1

    for j in range(low, high): # loop though the array 
        if pivot >= arr[j]: # check if the pivot is greater than current element then increment i and swap with j
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1] # now all elements less than pivot are before i so we interchange i+1 with pivot 
    return i+1 # return the pivot element location
        

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if high > low: # if high is greater than low
        part = partition(arr, low, high) # fetch the pivot location
        quickSort(arr, low, part-1) # and run the sort for elements on both sides of pivot
        quickSort(arr, part+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
