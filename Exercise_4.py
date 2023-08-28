# Time complexity: O(n logn)
# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  if(len(arr)>1):
    #write your code here
    size=len(arr)
    mid=int(size/2)

    l=arr[0:mid]
    r=arr[mid:size]

    mergeSort(l)
    mergeSort(r)
    i=j=k=0 
   
    new=[]
    while(i<len(l) and j<len(r)):
      if(l[i] <= r[j]):
        t=l[i]
        arr[k]=t
        i+=1
      else:
        t=r[j]
        arr[k]=t
        j+=1
      k+=1
    while(i< len(l)):
      arr[k]=l[i]
      i+=1
      k+=1
    while(j<len(r)):
      arr[k]=r[j]
      j+=1
      k+=1
   


    
    


  
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)-1): 
      print("%d" %arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
