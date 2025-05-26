# Python program for implementation of Quicksort Sort 
  
# Time Complexity: Best, Average Case: O(n log n), Worst Case: O(n^2)
# Space Complexity: O(log n) due to the recursive stack space used by the algorithm

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        p_index = partition(arr, low, high)
        quickSort(arr, low, p_index - 1)
        quickSort(arr, p_index + 1, high)
  
# # Driver code to test above 
# arr = [10, 7, 8, 9, 1, 5] 
# n = len(arr) 
# quickSort(arr,0,n-1) 
# print ("Sorted array is:") 
# for i in range(n): 
#     print ("%d" %arr[i]), 
  
 
