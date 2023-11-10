# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):

    #write your code here
    p_index=low
    pivot=arr[p_index]

    while low<high:
        while low<len(arr) and arr[low]<=pivot:
            low=low+1
        while arr[high]>pivot:
            high=high-1

        if low<high:

            arr[low], arr[high] = arr[high], arr[low]

    arr[p_index], arr[high] = arr[high], arr[p_index]

    return high


# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here

    if low<high:
        pos=partition(arr, low, high)
        quickSort(arr, low, pos-1)
        quickSort(arr, pos+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
