# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = low - 1
    p=arr[high]
    for j in range(low, high):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    i+=1
    return i
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, pivot + 1, high)
        quickSort(arr, low, pivot - 1)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted arr is:", arr) 
  
 
