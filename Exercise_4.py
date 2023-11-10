# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : Yes, conceptually I forgot how merge sort works so I watch video to understand
#but still had few doubts so refered google

# Python program for implementation of MergeSort 
def mergeSort(arr):
  #Checking whether array of length is greater than 1
  if len(arr) > 1:
    #Finding midpoint of array then partition array into a left_partition and a right_partition.
    mid = len(arr)//2
    Left_partition = arr[:mid]
    Right_partition = arr[mid:]
    mergeSort(Left_partition)
    mergeSort(Right_partition)
  
    i = j = k = 0
    #Executes the while loop if both pointers i and j are less than the length of the left and right array
    while i < len(Left_partition) and j < len(Right_partition):
      #Compare the elements at every position of both sides during each iteration
      if Left_partition[i] < Right_partition[j]:
        arr[k] = Left_partition[i]
        i += 1
      else:
        arr[k] = Right_partition[j]
        j += 1
      k += 1
    while i < len(Left_partition):
      arr[k] = Left_partition[i]
      i += 1
      k += 1

    while j < len(Right_partition):
      arr[k] = Right_partition[j]
      j += 1
      k += 1

  

  
# Code to print the list 
def printList(arr):
  print(arr)
   
    
   
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is:")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ") 
    printList(arr) 
