# Time Complexity : O(nlogn)
# Space Complexity : O(N) as extra space is used to create arrays for the halves of the original array
# Did this code successfully run on Leetcode : I did not find this exact problem on Leetcode
# Any problem you faced while coding this : This problem is not very intuitive and requires a deeper understanding of recursion


# Python program for implementation of MergeSort 
def mergeSort(arr, l, m, r):
  #write your code here

  n1 = m - l + 1  # shows the number of elements in the left half
  n2 = r - m   # shows the number of elements in the left half

  left = [0] * n1
  right = [0] * n2

  # dividing given list into 2 halves, left and right
  for i in range(n1):
    left[i] = arr[l+i]

  for j in range(n2):
    right[j] = arr[m + 1 + j]

  i = 0
  j = 0
  k = l

  # time complexity of this function is O(N) 
  # as we're looping through all elements of the list to get the sorted list
  # combining the left and right halves in sorted order
  while i < n1 and j < n2:
    if left[i] <= right[j]:  # to put the elements in sorted order when we merge
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k += 1

  # if any elements remain from the left half
  while i < n1:
    arr[k] = left[i]
    i += 1
    k += 1

  # if any elements remain from the right half
  while j < n2:
    arr[k] = right[j]
    j += 1
    k += 1 
    

  
# Code to print the list 
def printList(arr, l, r): 
    #write your code here
    if l < r:
      m = (l + (r - 1 ))//2
      printList(arr, l, m)
      printList(arr, m+1, r)
      mergeSort(arr, l, m, r)

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7] 

    print("\nGiven array is:")  
    for i in range(len(arr)): 
      print(str(arr[i]), end=" ")  

    printList(arr, 0, len(arr) - 1) 

    # mergeSort(arr, 0, (len(arr) - 1) // 2, len(arr) - 1) 
    
    print("\n\nSorted array is: ")
    for i in range(len(arr)):
      print(str(arr[i]), end=" ") 
    print("\n")

    # printList(arr, 0, len(arr) - 1) 
