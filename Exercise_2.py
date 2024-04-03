# Time Complexity : O(n log n)
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode: I ran this code in VS Code editor in my local machine
# Any problem you faced while coding this: No

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]

    # Set a pointer 1 position before the beginning of array
    i = low - 1

    for j in range (low, high):
        if arr[j] < pivot:
            i = i+1
            #Swap element of incremented i and j
            arr[i], arr[j] = arr[j], arr[i]
    # Finnaly swap element at pivot with i+1
    arr[i+1],arr[high] = arr[high], arr[i+1]

    # Returns starting position for next partition
    return i+1
 
# Function to do Quick sort 
def quickSort(arr,low,high):
    if(low<high):
        pi = partition(arr, low, high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high) 
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
