# Python program for implementation of Quicksort Sort 

# give you explanation for the approach

# Time complexity - O(n^2)
# Space complexity - O(n)

def partition(arr,low,high):
    #write your code here
    pivot = arr[high] # last element is chosen as pivot
    i, j = low, high - 1

    while i < j:
        while i < high and arr[i] < pivot: #find left element that is bigger than pivot element
            i += 1 
        while j > low and arr[j] >= pivot: # find right element that is lesser than pivot element
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i] # swap left and right elements
    
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i] # swap elements at index i and pivot element
    
    return i

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if len(arr) == 1: #only one element in sub array. nothing left to sort
        return arr
    if low < high:
        partitionIndex = partition(arr, low, high)
        quickSort(arr, low, partitionIndex - 1) #quicksort on left sub array
        quickSort(arr, partitionIndex + 1, high ) #quicksort on right sub array
    return arr

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
