# Python program for recursively implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(array,low,high):
    pivot = array[high]

    i = low-1 

    for j in range(low, high):
        if array[j] <= pivot:
            i+=1 
            array[i] , array[j] = array[j] , array[i]
    
    array[i+1] , array[high] = array[high], array[i+1]
    return i+1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
# Driver code to test above 
# this looks like in place sorting! 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])