# Python program for implementation of MergeSort 
def mergeSort(arr):
  # TC O(nlogn)
  # SC O(n)
  #write your code here
  if len(arr) <= 1:
    return
  mid = len(arr) // 2
  left, right = arr[:mid], arr[mid:]

  mergeSort(left)
  mergeSort(right)
  merge(arr, left, right)

def merge(arr, left, right):
  i = j = k = 0
  # this loop is responsible to check item in each of the left and right sorted lists 
  # and copying smaller element first to `arr`
  while i < len(left) and j < len(right) :
    # loop over left and right lists, if any of the list is exhausted, loop should end
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k +=1
  
  # if left list has any elements remaining
  while i < len(left):
    arr[k] = left[i]
    i+=1
    k+=1
  # if left list has any elements remaining
  while j < len(right):
    arr[k] = right[j]
    j+=1
    k+=1
  
  
# Code to print the list 
def printList(arr): 
  # time O(n)
  # space O(1)
  #write your code here
  for i in range(len(arr)):
    print(arr[i], end="\n")

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
