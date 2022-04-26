# Python program for implementation of MergeSort 
#Time complexity: O(nlogn)
#Space complexity: O(n)

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2

  left = arr[:mid]
  right = arr[mid:]

  mergeSort(left)
  mergeSort(right)

  merge_two_sorted_lists(left, right, arr)
  #write your code here

def merge_two_sorted_lists(a,b,arr):
  i = j = k = 0
  while i < len(a) and j < len(b):
    if a[i] <= b[j]:
      arr[k] = a[i]
      i += 1
      k += 1
    else:
      arr[k] = b[j]
      j += 1
      k += 1
  while i < len(a):
    arr[k] = a[i]
    i += 1
    k += 1
  while j < len(b):
    arr[k] = b[j]
    j += 1
    k += 1

# Code to print the list 
def printList(arr): 
    for i in arr:
      print(i)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n")
    printList(arr) 
