# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pidx = high
    i = low
    for j in range(low, high):
        if arr[j] < arr[pidx]:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[i], arr[pidx] = arr[pidx], arr[i]
    return i

  
# Function to do Quick sort 
def quickSort(arr,low,high):
    if high-low+1 <= 1:
        return
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
  
 
