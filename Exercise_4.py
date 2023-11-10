"""
Time Complexity : O(nlogn)
Space Complexity : O(n) 
Any problem you faced while coding this :yes
Your code here along with comments explaining your approach
""" 
# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:

    mid = len(arr)//2
    left = arr[0:mid]
    right = arr[mid: len(arr)]

    #Dividing the array in two halves
    mergeSort(left)
    mergeSort(right)

    l  = r = m = 0
    #copying data to temp array from Left & Right arrays
    while l < len(left) and r < len(right):
      if left[l] < right[r]:
        arr[m] = left[l]
        l +=1
      else:
        arr[r] = right[r]
        r += 1
      m +=1 

    #check for left-out elements in left array
    while l < len(left):
      arr[m] = left[l]
      l +=1
      m +=1

    #check for left-out elements in right array
    while r < len(right):
      arr[m]  = right[r]
      r += 1
      m += 1


# Code to print the list 
def printList(arr): 
  if len(arr) == 0:
    return 

  for i in range(len(arr)):
    print(arr[i], end = " ")
  print()

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
