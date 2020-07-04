# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    l = low-1
    pivot = arr[high]
    for k in range(l, high):
        if arr[k]<=pivot:
            l +=1
            arr[l],arr[k] = arr[k], arr[l]
    arr[l],arr[high] = arr[high], arr[l]
    return l


# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        pos = partition(arr,low,high)
        quickSort(arr,low,pos-1)
        quickSort(arr,pos+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
