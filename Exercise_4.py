#Space Complexity: O(1) ... where n is the number of elements
#Time Complexity: O(n log n) ... where n is the number of elements
#The code did run successfully

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
    start = 0
    end = len(arr)
    mid = (start + end)//2          #used for partitioning(division)
    
    left_half = arr[:mid]            #left partition      
    right_half = arr[mid:]           #right partition
    
    mergeSort(left_half)             #to recursively sort the left partition until we have only one element left
    mergeSort(right_half)            #to recursively sort the right partition until we have only one element left
    
    i = 0
    j = 0
    k = 0
    
    while i < len(left_half) and j < len(right_half):     #comparing the elements of left and right partition and combining them (conquer)
      if left_half[i] <= right_half[j]:
        arr[k] = left_half[i]
        k += 1
        i += 1
      else:
        arr[k] = right_half[j]
        k += 1
        j += 1
        
    while i < len(left_half):                             #to add remaining elements if any from the left partition
      arr[k] = left_half[i]
      k += 1
      i += 1
      
    while j < len(right_half):                            #to add remaining elements if any from the right partition
      arr[k] = right_half[j]
      k += 1
      j += 1
  
# Code to print the list 
def printList(arr): 
    for item in arr:
      print(item)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
