# Time Complexity : O(n log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No issues


# Python program for implementation of MergeSort 
def mergeSort(arr):
    # if the list has more than one element, split and sort
    if len(arr) > 1:
        mid = len(arr) // 2 # find midpoint
        left = arr[:mid]    # left half
        right = arr[mid:]   # right half

        mergeSort(left)     # sort left half
        mergeSort(right)    # sort right half
    
      # merge sorted halves back into arr
        i = j = k = 0
      # pick smaller element from left or right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
      # if any items left in left half, add them
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

      # if any items left in right half, add them
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

  
# Code to print the list 
def printList(arr): 
    # print all elements on one line
    for val in arr:
        print(val, end=' ')
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
