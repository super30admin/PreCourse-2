# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr)>1:
    mid = len(arr)//2

    l = arr[0:mid]
    h = arr[mid:]

    mergeSort(l)
    mergeSort(h)

    #merging lists
    i=j=k=0
    
    #Comparing and adding elements to list
    while i < len(l) and j<len(h):
      if l[i] <= h[j]:
        arr[k] = l[i]
        i += 1
      else:
        arr[k] = h[j]
        j += 1
      k += 1
    
    #adding remaining elements to list
    while i < len(l):
      arr[k] = l[i]
      i += 1
      k += 1

    while j < len(h):
      arr[k]=h[j]
      j += 1
      k += 1

  
# Code to print the list 
def printList(arr): 

    #write your code here
    for i in arr:
      print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
