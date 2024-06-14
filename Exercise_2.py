#Time Complexity : O(nlogn)
# Space Complexity : O(logn)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort Sort  
# give you explanation for the approach

#This function takes the last element of the array (arr[high]) as the pivot, places the pivot element at its correct position in sorted array, and places all smaller elements (smaller than pivot) to the left of the pivot and all greater elements to the right of the pivot.
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    pindex = low
    for k in range(low,high):
        if arr[k] <= pivot:
            arr[pindex],arr[k] = arr[k],arr[pindex]
            pindex += 1
    # Swap arr[pindex] and arr[high] to place the pivot in its correct position
    arr[pindex],arr[high] = arr[high],arr[pindex]
    return pindex

# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
    if low < high:
        pindex = partition(arr,low,high)
        #Sorting the left side of the array
        quickSort(arr,low,pindex-1)
        #Sorting the right side of the array
        quickSort(arr,pindex+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
