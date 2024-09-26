# Python program for implementation of MergeSort 
"""
// Time Complexity : O(nlogn)
// Space Complexity : O(nlogn)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None
// Your code here along with comments explaining your approach
Algorithm explanation
Merge

Mergesort
- We divide the arr into two halves untill we reach single element
- Left half gets the array elements till the mid
- Right half gets the array elements from mid till the end

Merge
- Using the left and right half of the array, we place the elements in order
- Initialize i,j,k to track the left, right and inplace arr
- while i < len(left) and j < len(right)
    - if left[i] <= right[j] then arr[k] = left[i] , i+=1
    else
        arr[k] = right[j], j+=1
- While there are elements remaining in the left, add to arr using k
- While there are elements remaining in the right, add to arr using k
"""

def merge(arr,left,right):
    n1 = len(left)
    n2 = len(right)
    i,j,k = 0,0,0

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while i < n1:
        arr[k] = left[i]
        k+=1
        i+=1

    while j < n2:
        arr[k] = right[j]
        k+=1
        j+=1


def mergeSort(arr):
    #write your code here
    N = len(arr)
    if N > 1:
        mid = N // 2
        mergeSort(arr[:mid])
        mergeSort(arr[mid:])
        merge(arr,arr[:mid],arr[mid:])
  
# Code to print the list 
def printList(arr):
    
    #write your code here
    for i in range(len(arr)):
        print(arr[i],end= " ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(arr)
