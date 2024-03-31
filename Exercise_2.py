# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time Complexity : O(nlogn)
# Space Complexity : O(1)

def partition(arr,low,high):
    pivot = low
    i = low
    j = high

    while (i < j):
        while(arr[i] < arr[pivot] and i <= high):
            i += 1
        while (arr[j]> arr[pivot] and j >= low):
            j -= 1
        if (i < j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[pivot],arr[j] = arr[j],arr[pivot]
    return j


# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if (low<high):
        j = partition(arr, low, high)
        quickSort(arr, low, j-1)
        quickSort(arr,j+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),
  
 
