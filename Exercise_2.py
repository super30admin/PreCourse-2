# Time Complexity : partition() - O(n), Quicksort() - Average Case O(n log n)
# Space Complexity : O(h) = O(log n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : Yes


# Your code here along with comments explaining your approach

'''
1. I have done partition by chosing the last element to be the pivot element initially and initializing,
    a variable pIndex=0, that would actually be the pivot element. Element from start to end-1 are iterated,a nd compared with initialized pivot elemnt, and if elements are lesser than pivot element, pIndex is increase.

2. Then quickosrt is performed, which is classic pre-order Tree traversal where each node(governed by start and end position of the array), is partitioned, and then scaled left part start to pivot-1

3.At last the right part is covered from p+1 to end
'''


# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):

    pivot_element = arr[high]
    pIndex = low


    for i in range(low, high):

        if arr[i] < pivot_element:

            temp = arr[i]
            arr[i] = arr[pIndex]
            arr[pIndex] = temp

            pIndex += 1


    temp = arr[pIndex]
    arr[pIndex] = arr[high]
    arr[high] = temp


    return pIndex
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high):

    if low >= high:
        return

    pivot_element = partition(arr, low, high)
    quickSort(arr,low, pivot_element-1)
    quickSort(arr,pivot_element+1, high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
