# Python program for implementation of MergeSort 
# Time complexity O(nlogn)
# Space complexity O(n)

def mergeSort(arr):

  if len(arr)>1:
     #devide the arr in 2 halves
    mid= len(arr)//2
    l1=arr[:mid]

    l2=arr[mid:]
  #recursively call merge sort on both of them for sorting
    mergeSort(l1)
    mergeSort(l2)

    a=b=c=0

    while a < len(l1) and b < len(l2):
      # if value at index a of l1 is lesser than value at index b of l2 
      if l1[a] < l2[b]:
        arr[c] = l1[a]
        a += 1
       
      else:
        arr[c] = l2[b]
        b +=1
      c +=1

#if l1 has more elements remaining
    while a < len(l1):
      arr[c] = l1[a]
      a +=1
      c +=1

  #if l2 has more remaining elements 
    while b < len(l2):
      arr[c] = l2[b]
      b +=1
      c +=1

  
# Code to print the list 
def printList(arr): 
  for c in range(len(arr)):
    print(arr[c])
  print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
