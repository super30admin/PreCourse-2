# Time Complexity : Average time complexity is O(n log(n)) since it partitions the array and recursively sort the sub arrays
# Partioning step takes linear time and there are log(n) recursive calls on average.
# Space Complexity : Average space complexity is O(log(n)) since there are log(n) splits on average and we need extra memory at each split

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    # Selecting middle element as pivot
    mid = (low+high)//2
    pivot = arr[mid]

    while low <= high:
        # the low pointer starts at the beginning of the array and stops at an element that is greater than or equal to the pivot
        while arr[low] < pivot:
            low+=1
        # high pointer starts from the end of the array and stops at an element that is smaller than pivot
        while arr[high] > pivot:
            high-=1
        # Swap the elements at high at low pointers if the low pointer is still to the left of the low pointer
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low+=1
            high-=1
    # At the end of the while loop, low pointer moves to the correct position of the pivot element in sorted array
    return low 
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low >= high:
        return 
    
    index = partition(arr, low, high)
    # Recursively call the function on left and right sides of pivot.
    quickSort(arr, low, index-1)
    quickSort(arr, index, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
