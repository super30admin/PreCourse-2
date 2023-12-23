# Time Complexity : ON(logn) - As the array is split into two halves and takes linear time to merge the halves.
# Space Complexity : O(1) - No additional space is used
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Not really
# Python program for implementation of MergeSort 

def merge(arr, low, mid, high):
    left, right = low, mid+1
    result = []
    while left<=mid and right<=high:
        if arr[left] <= arr[right]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right])
            right += 1 
    
    # Add remaining elements from the left subarray
    while left <= mid:
        result.append(arr[left])
        left += 1

    # Add remaining elements from the right subarray
    while right <= high:
        result.append(arr[right])
        right += 1

    # Update the original array with the merged result
    for i in range(len(result)):
        arr[low + i] = result[i]

def mergeSort(arr, low, high):
    if low>=high:
        return
    mid = (low+high)//2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i])
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
