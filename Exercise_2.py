# Python program for implementation of Quicksort Sort 
#Time complexity:Best -> O(n logn) Worst -> O(n2)
#Space complexity:Best -> O(logn) Worst -> O(n)
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high] # choosing last elemrnt as pivot
    i = low - 1 # pointer for smaller elements
    for j in range(low,high): #traverse from low to high
        if arr[j] <= pivot: #if elements smaller or equal to pivot
            i += 1 #increment low pointer
            arr[i],arr[j] = arr[j],arr[i] #swapping lower element to the left
    arr[i+1],arr[high] = arr[high],arr[i+1] #swapping pivot element to the correct position
    return i+1 #returning partition index

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pivot_index = partition(arr, low, high)  # Find pivot position
        quickSort(arr, low, pivot_index - 1)  # Recursively sort left half
        quickSort(arr, pivot_index + 1, high) #recursively sort right
      
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
print("Before Sorting: ",arr)
n = len(arr)
quickSort(arr,0,n-1) 
print("After Sorting: ",arr)
  
 
