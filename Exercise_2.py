# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    #picking the last element as pivot
    for i in range(low,high):
      if arr[i] <= arr[high]:
        arr[i], arr[low] = arr[low], arr[i]
        low += 1
    arr[low], arr[high] = arr[high], arr[low]
    return low
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    #divide the arr into 2 parts and call the quicksort function recursively
    if len(arr)>1:
      mid = partition(arr,low,high)
      quickSort(arr,low,mid-1)
      quickSort(arr,mid+1,high)
    return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
