# Python program for implementation of MergeSort
# Time Complexity :O(n log n)
# Space Complexity :O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None
# Your code here along with comments explaining your approach: The code implements Merge Sort, a divide-and-conquer algorithm that recursively splits the array into two halves until each subarray has one element. The mergeSort function then merges these sorted halves by comparing elements one by one and placing them in the correct order. The printList function is just for displaying the array, and the driver code shows the array before and after sorting.


def mergeSort(arr):
  #write your code here
  if len(arr) > 1:
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j +=1
      k += 1
    
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
  for i in range(len(arr)):
    print(arr[i], end = " ")
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
