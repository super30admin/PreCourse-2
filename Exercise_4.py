
# Python program for implementation of MergeSort 
def merge(arr,l,m,r):
  #write your code here
  n1 = m - l + 1
  n2 = r - m

  L = [0] * n1
  R = [0] * n2

  for i in range(0, n1):
    L[i] = arr[l + i]

  for j in range(0, n2):
    R[j] = arr[m + 1 + j]

  i = 0
  j = 0
  k = l

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1
   
def Sort(arr,l,r):
  #write your code here
  if l < r:
    m = (l + r) // 2
    Sort(arr, l, m)
    Sort(arr, m + 1, r)
    merge(arr, l, m, r)

  
# Code to print the list 
def printList(arr): 
  #write your code here
  print(arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    Sort(arr,0,len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
