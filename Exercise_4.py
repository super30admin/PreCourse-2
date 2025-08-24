# Python program for implementation of MergeSort 
# // Time Complexity : 
# // Space Complexity : 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No
# merge sort : first divide array into half parts, and recurively sort the each half and then merge the sorted halves into one sorted array
# since adding the sorted halves into array a new array where the elemsts are sorted  the space complexity is O(n) 
def mergeSort(arr):
  
  #write your code here
  if len(arr)<2: # split array into equal parts
        return arr
        
  mid = len(arr)//2
  
  left_half = arr[:mid]
  right_half = arr[mid:]
  
  mergeSort(left_half)
  mergeSort(right_half)
  
  i = j = k = 0
  
  while i< len(left_half) and j < len(right_half): # sort each array and add the sorted elements into arr
      if left_half[i] < right_half[j]:
          arr[k] = left_half[i]
          i+=1
      else: 
          arr[k] = right_half[j]
          j+=1
      k += 1
      
  while i< len(left_half): # adding rest of the elements in the array
      arr[k] = left_half[i]
      i+= 1
      k += 1
      
  while j< len(right_half):
      arr[k] = right_half[j]
      j+= 1
      k+= 1 
  
  return arr

  
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
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
