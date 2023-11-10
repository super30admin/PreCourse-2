# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    index = low
    pivot=arr[index]
    while low<=high:
        while low<=high and arr[low]<=pivot :
            low = low+1
        while low<=high and arr[high]>=pivot:
            high = high-1
        if low<=high:
            arr[low],arr[high]=arr[high],arr[low]
    arr[index],arr[high]=arr[high],arr[index]
    return high

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low<high:
        pivot_loc = partition(arr,low,high)
        quickSort(arr,low,pivot_loc)
        quickSort(arr,pivot_loc+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
