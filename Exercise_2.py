# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = (low-1)  
    pivot = arr[high]     
    for j in range(low, high): 
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
def quickSort(arr,low,high):
    if(low<high):
        if len(arr) == 1: 
            return arr 
    if low < high:
        pi = partition(arr, low, high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),

# Explanation:
# Pivot element is the last element - place this element at its right position first
# all the elements that are less than pivot go to the left 
# all the elements greater than pivot go to the right