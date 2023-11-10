# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,l,h):
    pivot = arr[h]
    index = l
    for i in range(l, h, 1):
        if arr[i] < pivot:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    arr[index], arr[h] = arr[h], arr[index]
    return index

    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low<high:
        partitionIndex = partition(arr,low,high)
        quickSort(arr,low,partitionIndex-1)
        quickSort(arr,partitionIndex+1,high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
