# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[high]  # last element as the pivot
    i = low - 1        # smaller element

    for j in range(low, high):
        # if the current element is smaller than or equal to the chosen pivot
        if arr[j] <= pivot:
            i += 1     
            arr[i], arr[j] = arr[j], arr[i]  # swapping elements

    # swapping the pivot element with the element at i+1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
