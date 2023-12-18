
#Time complexity of Quicksort is O(n log n)
#Space complexity of Quicksort is O(log n)
# Python program for implementation of Quicksort Sort 
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]  # Selecting the rightmost element as the pivot
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            # Swap arr[i] and arr[j]
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap arr[i+1] and arr[high] (pivot element)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

    #write your code here

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pi = partition(arr, low, high)   #getting pivot index
        
        # Recursive calls to sort the sub-arrays
        quickSort(arr, low, pi - 1)  # for the Elements before 
        quickSort(arr, pi + 1, high)  # for the Elements after 
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
