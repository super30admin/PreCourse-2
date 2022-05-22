'''
Time Complexity: O(nlog(n))
Space Complexity: O(n)
Problem: Merging two lists using 
        3 pointers.
'''
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    Left = arr[0:mid]
    Right = arr[mid:len(arr)]
    mergeSort(Left)
    mergeSort(Right)
    l = 0
    r = 0
    k = 0
    while l < len(Left) and r < len(Right):
      if Left[l] <= Right[r]:
        arr[k] = Left[l]
        l += 1
      else:
        arr[k] = Right[r]
        r += 1
      k += 1
    
    if r == len(Right):
      while l < len(Left):
        arr[k] = Left[l]
        l += 1
        k += 1
    else:
      while r < len(Right):
        arr[k] = Right[r]
        r += 1
        k += 1


# Code to print the list 
def printList(arr):
  for val in arr:
    print(val)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
