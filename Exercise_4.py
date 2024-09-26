# Time Complexity :O(nLog(n))
# Space Complexity :O(n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no


# Your code here along with comments explaining your approach
def merge(L,H,arr):
  i = j = k = 0
  while i < len(L) and j < len(H):
    if L[i] <= H[j]:
      arr[k] = L[i]
      i+=1
    else:
      arr[k] = H[j]
      j+=1
    k+=1
  while i < len(L):
    arr[k] = L[i]
    i+=1
    k+=1
  while j < len(H):
    arr[k] = H[j]
    j+=1
    k+=1

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) <2:
    return
  L = []
  H = []
  for i in range(len(arr)):
    if i < len(arr)//2:
      L.append(arr[i])
    else:
      H.append(arr[i])
  mergeSort(L)
  mergeSort(H)
  merge(L,H,arr)
  
# Code to print the list 
def printList(arr): 
  for i in arr:
    print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
