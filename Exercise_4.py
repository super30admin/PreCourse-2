# Python program for implementation of MergeSort
def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1
 
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
def mergeSort(arr):
  w  = 1
  n = len(arr)
  while w < n:
    low = 0
    while low < n:
      r = min(low + (w*2 - 1), n - 1)
      m = int((low + r)/2)
      if w > n//2:
        m = r - (n%w)
      merge(arr, low, m, r)
      low += w * 2
    w *= 2
  return arr      
  #write your code here
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
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
