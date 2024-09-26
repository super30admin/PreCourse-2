# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # 1. slecting last element as the pivot
    p = arr[high]
    # 2. set index of smaller element as i
    i = (low -1)
    # 3. Loop over j to compare it with p: if greater/equal, move i by one and swap: 
    # if smaller, do nothing
    for j in range(low, high):
        if arr[j] <= p:
            i=i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        
        # get the index of partition
        p= partition(arr, low, high)
        
        # recursively do it for the left & right sides of partition
        quickSort(arr, p+1, high) 
        quickSort(arr, low, p-1) 
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
