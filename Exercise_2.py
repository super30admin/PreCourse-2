# Time Complexity : O(nlogn) as I am using randomized partition method
# Space Complexity : O(1) as its in place sorting
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Had to brush up the algorithm of quick sort


# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach: 
# First I used the non randomised version of partitioning that will always take the end item of the array as the pivot. I read in a blog that choosing the pivot randomly is a good idea as it avoids attaining the worst case even if the array is already sorted i.e. avoiding the time complexity of O(n^2). Quick sort is not a stable sorting algo but merge sort is.

import random

def randomizedPartition(arr,start,end):
    pivot_index = random.randint(start,end)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    partition_index = partition(arr,start,end)
    return(partition_index)

def partition(arr,start,end):
    #write your code here
    pivot = arr[end]
    partition_index = start
    for i in range(start,end):
        if arr[i]<=pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1
    arr[partition_index], arr[end] = arr[end], arr[partition_index]
    return partition_index

# Function to do Quick sort 
def quickSort(arr,start,end): 
    
    #write your code here
    if start<end:
        partition_index = randomizedPartition(arr,start,end)
        quickSort(arr,start,partition_index-1)
        quickSort(arr,partition_index+1,end)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
  
 
