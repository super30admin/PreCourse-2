# Time Complexity : O(n log n)
# Space Complexity : O(log n)

# Approach:
# I have implemented the merge sort algorithm using recursive approach.
# First I have divided the array into two halves and then called the merge sort function recursively 
# on the two halves.
# Then I have merged the two halves by comparing the elements of the two halves and then
# merged the two halves into a single sorted array.
# Finally, printed the sorted array.

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
    mid = len(arr) // 2
    left_array = arr[:mid]
    right_array = arr[mid:]
    mergeSort(left_array)
    mergeSort(right_array)

    # Merge the two halves
    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
      if left_array[i] < right_array[j]:
        arr[k] = left_array[i]
        i += 1
      else:
        arr[k] = right_array[j]
        j += 1
      k += 1
    
    while i < len(left_array):
      arr[k] = left_array[i]
      i += 1
      k += 1
    
    while j < len(right_array):
      arr[k] = right_array[j]
      j += 1
      k += 1
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
      print(arr[i], end=" ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
