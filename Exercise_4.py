# Python program for implementation of MergeSort 
# first we divide the array until there are array with only one item.
# Then merge. At first I got the concept but I did not undertsnad how to code it.
# I took help from gfg and implmemnted the code and handtraced the whole solution with numbers to undertstand it
# I struggle coding recursive problems and I need to improve on this
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
    l1 = arr[:len(arr)//2]
    l2 = arr[len(arr)//2:]

    mergeSort(l1)
    mergeSort(l2)
    i=j=k=0
    while i<len(l1) and j<len(l2):
      if l1[i] <= l2[j]:
          arr[k] = l1[i]
          i += 1
      else:
          arr[k] = l2[j]
          j += 1
      k += 1
    
    while i < len(l1):
       arr[k] = l1[i]
       i += 1
       k += 1
    while j < len(l2):
       arr[k] = l2[j]
       j += 1
       k += 1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i], end=" ")
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
