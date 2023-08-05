# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[high]
    i = low -1 
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pidx = partition(arr, low , high)
        quickSort(arr, 0, pidx-1)
        quickSort(arr, pidx+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
