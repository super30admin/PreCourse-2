# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
    count = 0                           # count all elements lower than element at low index
    for i in range(low + 1, high + 1):
        if arr[i] < arr[low]:
            count += 1
    swap(arr, low, low + count)

    pivot = low + count

    while (low < pivot and high > pivot):   # push all lower elements to left and all higher elements to right
        if (arr[low] >= arr[pivot]):
            if (arr[high] < arr[pivot]):
                swap(arr, low, high)
                low += 1
                high -= 1
            else:
                high -= 1
        else:
            low += 1

    return pivot                    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if (low >= high):       
        return
    pivot = partition(arr, low, high)  
    quickSort(arr, low, pivot)         
    quickSort(arr, pivot+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
