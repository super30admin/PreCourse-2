# Python program for implementation of MergeSort 
# Time complexity - O(nlogn)     Space complexity - O(n)

# In the mergeSort - if the n is greater than 1, dividing the given array into two halves left and right
# and left array is further divided to left and right until the length of respective left/right array is > 1
# Later, creating 3 pointers i, j, k for left, right and main array respectively
# comparing elements with left and right array and modifying main array according to that
def mergeSort(arr):
    n = len(arr)
    if n > 1:
        left = arr[:n//2]
        right = arr[n//2:]
        mergeSort(left)
        mergeSort(right)
        
        i = j = k = 0
        l = len(left)
        r = len(right)
        while i < l and j < r:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i, k = i+1, k+1
            else:
                arr[k] = right[j]
                j, k = j+1, k+1
        # checking for any missing items and adding them to final array
        while i < l:
            arr[k] = left[i]
            i, k = i + 1, k + 1
        while j < r:
            arr[k] = right[j]
            j, k = j + 1, k + 1
  
# Code to print the list 
def printList(arr):
      print(arr)

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
