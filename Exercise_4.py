# Python program for implementation of MergeSort
# Time Complexity : O(nlogn)
# Space Complexity : O(n) as n is length of arr, left and right
# Did this code successfully run on Leetcode : LC 912 yes
# Any problem you faced while coding this : NA
 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
 
         # Diving array into half
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
 
        # recursive sort the first and second half
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
 
        # loop, conquer, fill correct order
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        # just fill arr with leftover elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
        print(arr[i])
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)