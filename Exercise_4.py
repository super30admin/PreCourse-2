"""
# Time Complexity :  O(nLogN) - all cases

# Space Complexity : O(N) - to create the temporary array while merging elements

# Did this code successfully run on Leetcode : N/A, performed local testing

# Any problem you faced while coding this : 
> replacing elements after merging in temp array needs to be done with offset
> need to pass proper bounds (0, n -1), else got an index out of bounds error

"""

# Python program for implementation of MergeSort 


def mergeFn(arr, low, mid, high):
    res = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            res.append(arr[left])
            left += 1
        else:
            res.append(arr[right])
            right += 1
        
    while left <= mid:
        res.append(arr[left])
        left += 1
    
    while right <= high:
        res.append(arr[right])
        right += 1
    
    for i in range(len(res)):
        arr[low + i] = res[i]

def mergeSortFn(arr, low, high):
    if low >= high:
        return
    mid = (low + high)//2
    mergeSortFn(arr, low, mid)
    mergeSortFn(arr,mid+1, high)
    mergeFn(arr,low, mid, high)


def mergeSort(arr):
  
  #write your code here
  low = 0
  high = len(arr) - 1
  mergeSortFn(arr, low, high) 

  
# Code to print the list 
def printList(arr): 
    for x in arr:
        print(x, end=" ")
    print()
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
