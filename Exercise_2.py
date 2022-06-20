# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot,ptr=arr[high],low

    for i in range(low,high):
        if arr[i]<=pivot:
            arr[i],arr[ptr]=arr[ptr],arr[i]
            ptr+=1

    arr[ptr],arr[high]=arr[high],arr[ptr]
    return ptr
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr)==1:
        return arr

    if low<high:
        l=partition(arr, low, high)
        quickSort(arr, low, l-1)
        quickSort(arr, l+1, high)

    return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
