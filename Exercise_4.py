# Python program for implementation of MergeSort 
# Submitted by : Aryan Singh_RN12MAY2023
# Time Complexity : O(n logn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Not applicable
# Any problem you faced while coding this : No 

def mergeSort(arr):
# Check if array can be divided into sub-arrays
  if len(arr) > 1:
    # Find the middle index of the array
    mid = len(arr) // 2
    # Divide the array into left and right sub-arrays
    left = arr[:mid]
    right = arr[mid:]
    # Sort the left and right sub-arrays
    mergeSort(left)
    mergeSort(right)
    # Merge the left and right sub-arrays
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            arr[k] = left[i] 
            i += 1
        else: 
            arr[k] = right[j] 
            j += 1
        k += 1
    # Copy any remaining elements from the left sub-array
    while i < len(left): 
        arr[k] = left[i] 
        i += 1
        k += 1
    # Copy any remaining elements from the right sub-array
    while j < len(right): 
        arr[k] = right[j] 
        j += 1
        k += 1

 
  
# Code to print the list 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end="")
        if i != len(arr) - 1:
            print(" ", end="")
    print()
    
    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
