# Python program for implementation of Quicksort Sort 
# give you explanation for the approach

#Time Complexity:
# Best and Average Case: O(n log n)
# Worst Case: O(n^2) when the pivot is always the smallest or largest

# Space Complexity:
# O(log n) for recursion stack in best/average case
# O(n) in worst case (unbalanced partitions)
 

def partition(arr,low,high):

   #write your code here
    pivot = arr[high]  # choose last element as pivot
    i = low - 1         # index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # place pivot
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pi = partition(arr, low, high)   # partition index
        quickSort(arr, low, pi - 1)      # sort left half
        quickSort(arr, pi + 1, high)     # sort right half
  


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
  

