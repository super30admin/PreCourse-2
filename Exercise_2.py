# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here

    x = arr[high]
    k = low-1
    for i in range(low, high):
        if arr[i] <= x:
            k+=1
            arr[k], arr[i] = arr[i], arr[k]

    arr[k + 1], arr[high] = arr[high], arr[k + 1]
    return k+1
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    # return None
    if low<high:
        part = partition(arr, low, high)
    
        # recursive - on left of x
        quickSort(arr, low, part - 1)

        # recursive - on right of x
        quickSort(arr, part + 1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 