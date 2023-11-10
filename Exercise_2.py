# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    pIdx = low
    for i in range(low,high):
        if arr[i] <= pivot:
            arr[i],arr[pIdx] = arr[pIdx],arr[i]
            pIdx+=1
            # print(arr)
    arr[pIdx],arr[high] = arr[high],arr[pIdx]
    # print(arr)
    return pIdx
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
    if low > high:
        return
    pivotIndex = partition(arr,low,high)
    quickSort(arr, low, pivotIndex-1)
    quickSort(arr, pivotIndex+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
