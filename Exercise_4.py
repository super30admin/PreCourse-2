# Python program for implementation of MergeSort
''' Time complexity : O(n log n)
Space Complexity: O(n) - left and right array of size n/2


Did this code successfully run on Leetcode : -
Any problem you faced while coding this : No ''' 
def mergeSort(arr):
    #write your code here
    if len(arr) > 1:
        mid = len(arr) // 2 # find middle element
        left = arr[:mid]
        right = arr[mid:]

        # call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for left and right side
        i = 0
        j = 0
        
        # Iterator for the main array
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              arr[k] = left[i]
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1

# Code to print the list 
def printList(arr): 
  #write your code here
  for i in range(len(arr)):
    print(arr[i])
    
    
    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
