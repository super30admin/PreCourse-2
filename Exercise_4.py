# Python program for implementation of MergeSort 
#Time complexity: O(nlogn)
#Space complexity: O(n)
def mergeSort(arr):
  if len(arr)==1:
    return arr
  L=mergeSort(arr[:len(arr)//2])
  R=mergeSort(arr[len(arr)//2:])
  return merge(L,R)
# L -> 1, 4, 6    R-> 2,3
def merge(L,R):
  l=0
  r=0
  print(L,R)
  new_len=len(L)+len(R)
  res=[0]*new_len
  for i in range(new_len):
    if r>=len(R) or (l<len(L) and L[l]<R[r]):
      res[i]=L[l]
      l+=1
    else:
      res[i]=R[r]
      r+=1
  return res

  
def printList(arr):
  print(arr)

if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr=mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
