"""
Quick Sort:
I am taking last value of the array as the pivot
and rearranging all the values depending
if they are greater or lesser than the pivot
We will have a border value, everything to the left of the border will be smaller than the pivot
is the current number in consideration smaller than the pivot, if yes we will swap the value with the border
and then we advance both pointers i.e border and the current value in consideration.
if the current number is not smaller than the pivot then we just advance the value pointer else we swap the value with
the border and advance both pointers, when the list ends, we are going to swap the pivot with the border value, we will see
that the value left of pivot will be smaller than the pivot and values to the right of pivot will be greater than the
pivot. After partition we will be runnning the quick sort algorithm recursively and applyingquicksort on left list and right list
 till low becomes >=high
Time complexity: O(nsquared) worst, during first partition, one list has 1 element while rest has all the other elements
Space Complexity: I can't figure out
:return: Sorted Array
Issue: Not running on leetcode
"""
import random
def partition(arr,low,high):

    pivotindex=high
    # print("pivotindexis", pivotindex)
    border=low
    for i in range(low, high+1):
        if arr[i]<pivotindex:
            arr[i], arr[border]=arr[border], arr[i]
            border+=1
    arr[pivotindex], arr[border]=arr[border], arr[pivotindex]
    return border

# Function to do Quick sort 
def quickSort(arr,low,high):

   if low < high:
       pivotindex=partition(arr, low, high)
       quickSort(arr, low, pivotindex-1)
       quickSort(arr, pivotindex+1, high)

    #write your code here

# Driver code to test above 
arr = [5,1,1,2,0,0]
# arr=[1,1,0,2,3]
# arr=[5,2,3,1]
print("initial array is", arr)
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
