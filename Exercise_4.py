# Python program for implementation of MergeSort 
def helper_main(arr,l,m,r):

  l1 = arr[l:m+1]
  l2 = arr[m+1:]
  k = 1
  print(l1,l2)
  i, j = 0, 0
  if l1 == l2:
    while i<len(l1)-1 and j<len(l2)-1:
      if l1[i]>l2[j]:
        arr[k] = l2[j]
        j += 1
      elif l1[i]<l2[j]:
        arr[k] = l1[i]
        i += 1
      k += 1
      #print(i,j)
  
    while i<len(l1):
      arr[k] = l1[i]
      k += 1
      i += 1

    while j<len(l2):
      #print(k,j)
      arr[k] = l2[j]
      k += 1
      j += 1
  
def mergesort(arr,l,r):
  if l<r:
    m = (l)+(r-l)//2

    mergesort(arr,l,m)
    mergesort(arr,m+1,r)
    helper_main(arr,l,m,r)
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
