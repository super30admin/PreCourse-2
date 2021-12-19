# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
   pivot_element = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot_element:
            i = i+1
            #swap
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) == 1:
        return
    if (low < high):
        idx = partition(arr, low, high)
        quickSort(arr, low, idx - 1)
        quickSort(arr, idx + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
#arr = [8,6,1,12]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
