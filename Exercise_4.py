# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here

  if len(arr) > 1:

    mid = len(arr)//2

    l = arr[:mid]
    r = arr[mid:]

    mergeSort(l)

    mergeSort(r)

    a=b=c=0

    while a < len(l) and b < len(r):

      if l[a] < r[a]:
        arr[c] = l[a]
        a+=1

      else:
        arr[c] = r[b]
        b+=1

      c+=1

    while a < len(l):
      arr[c] = r[a]
      a+=1
      c+=1

    while b < len(r):
      arr[c] < r[b]
      b+=1
      c+=1



  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
      print(arr[i])
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
