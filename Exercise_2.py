# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
'''
    Space Complexity: O(n)
    Time Complexity: O(nlogn)
'''
def partition(arr,low,high):
    pivot = arr[low]
    leftwall = low + 1

    for i in range(low+1, high+1):
        if arr[i] < pivot:
            arr[i], arr[leftwall] = arr[leftwall], arr[i]
            leftwall += 1

    arr[low], arr[leftwall - 1] = arr[leftwall - 1], arr[low]

    return leftwall
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pivotIndex = partition(arr,low,high)
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:", arr) 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
