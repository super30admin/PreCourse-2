# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
def partition(arr,low,high):
    pivot, p = arr[high], low

    for i in range(low, high):

        if arr[i] <= pivot:    
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
    
    arr[p], arr[high] = arr[high], arr[p]
    return p
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)  # Recursively sorting the left values
        quickSort(arr, pi+1, high)  # Recursively sorting the right values
    return arr
    #write your code here
  
# Driver code to test above 
arr = [10, 2, 7, 8, 0, 100, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
