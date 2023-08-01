# Time Complexity : O(nlogn) for average/best case. O(n*n) for worst case
# Space Complexity : O(logn) for average/best case. O(n) for worst case
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high] #Selecting the last element of the array as the pivot element
    i = low-1 
    for j in range(low,high): #Traversing through all the elements
        if arr[j] <= pivot: #Comparing the elements with the pivot
            i += 1 #If the element is less than or equal to pivot, swap it with the element at i+1 index
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])  #Swap the pivot element to its correct sorted position
    return i+1 #return the pivot index

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        pivot_index = partition(arr, low, high) #Partition the array and get the pivot index

        #Recursively sort the sub-arrays on the left and right of the pivot
        quickSort(arr, low, pivot_index-1) 
        quickSort(arr, pivot_index+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 