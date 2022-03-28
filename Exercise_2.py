# Time Complexity : O(nlogn)
# Space Complexity :O(logn)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach ---->

# The idea behind the approach is to find a pivot element from the given array, which is then moved to
# a location where it will be if the array gets sorted. After this, the sub arrays before and after the pivot 
# are made to follow the same approach, recursively to get the complete array sorted. Here, thr last element of the
# array is being choosen as the pivot


def partition(arr,low,high):
    #last index being taken as pivot, bigInx is the index of value greater than pivot
    bigInx = low-1
    pivot = arr[high]

    for smlInx in range(low,high):
        # if value less than pivot, values at smlInx and bigInx are interchanged
        if arr[smlInx] <= pivot:
            bigInx += 1
            arr[bigInx], arr[smlInx] = arr[smlInx], arr[bigInx]

    #finally pivot value and the index next to bigInx are interchanged
    arr[bigInx+1], arr[high] = arr[high], arr[bigInx+1]  
    return bigInx+1

# Function to do Quick sort 
def quickSort(arr,low,high):
    if len(arr) == 1:
        return arr
    
    if low < high:
        #once a pivot gets sorted, the right and left subarrays are sorted recursievly
        partitionInx = partition(arr,low,high)

        quickSort(arr,low,partitionInx-1)
        quickSort(arr,partitionInx+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
