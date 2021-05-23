# Python program for implementation of MergeSort 
# Time complexity : O(nlogn)
def mergeSort(arr):
  #write your code here
  # recursive function which divides array into subparts(divide and conquer)
  # call merge on each of the subparts to get sorted subparts
  n = len(arr)
  if n == 1:
    return arr
  mid = n//2
  a1 = arr[:mid]
  a2= arr[mid:]
  a1 = mergeSort(a1)
  a2 = mergeSort(a2)
  return merge(a1,a2)

def merge(a,b):
  c = []
  i,j = 0,0
  # Parse through loop till end of one of the lists a or b
  while i < len(a)  and j < len(b):
    if a[i] > b[j]:
      c.append(b[j])
      j += 1
    else:
      c.append(a[i])
      i += 1
  # the remaining elements(if left) in list a would be sorted, so add to c
  while i<len(a):
    c.append(a[i])
    i+=1
  # the remaining elements(if left) in list b would be sorted, so add to c
  while j< len(b):
    c.append(b[j])
    j+=1
  return c 
# Code to print the list 
def printList(arr): 
    #write your code here
    print(arr)
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
