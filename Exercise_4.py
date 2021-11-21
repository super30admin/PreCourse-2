#Time Complexity - O(nlogn)
def merge(arr,l,m,r):
  n1 = m - l + 1
  n2 = r - m
  L = [0] * n1
  R = [0] * n2
  for i in range(n1):
    L[i] = arr[i+l]
  for j in range(n2):
    R[j] = arr[m+1+j]
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
  while j < n1:
    arr[k] = R[j]
    j += 1
    k += 1
def mergeSort(arr,l,r):
  if l < r:
    m = (l+(r-1)) // 2
    mergeSort(arr,l,m)
    mergeSort(arr,m+1,r)
    merge(arr,l,m,r)
  return arr
def printList(arr):
  i = 0
  for i in range(len(arr)):
    print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0,len(arr) - 1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
