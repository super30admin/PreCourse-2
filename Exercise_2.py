# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Time Complexity O(n**2) worst case, O(nlogn) average case
def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    j = high
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j


  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        part = partition(arr,low,high)
        quickSort(arr,low,part)
        quickSort(arr,part+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
