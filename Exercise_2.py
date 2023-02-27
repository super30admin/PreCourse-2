# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    pindex = low
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex += 1
    arr[pindex], arr[high] = arr[high], arr[pindex]
    return pindex
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low >= high:
        return arr
    pindex = partition(arr, low, high)
    quickSort(arr, low, pindex - 1)
    quickSort(arr, pindex + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
