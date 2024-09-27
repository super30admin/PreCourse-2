# Python program for implementation of Quicksort Sort

"""

  Student : Shahreeen Shahjahan Psyche

  Running Complexity : O(NlogN)
  Memory Complexity: O(log N)

  The Code Ran Successfully

"""
  
# Quick sort is similar to merge sort. Here we just select a pivot point to sort the array. I have selected the last element of an array every time as pivot.


# This function selects the pivot point, then rearranges the array according to the pivot. All the smaller or equal ones are shifted to left and all the greater
# one are shifted to right. Then it returns the division position of theese 2 sides.
def partition(arr,low,high):

    p = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= p:
            i = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp

    return i + 1
  


# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        p = partition(arr, low, high)

        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)
    

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
