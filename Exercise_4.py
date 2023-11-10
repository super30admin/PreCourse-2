# Python program for implementation of MergeSort 
# time complexity is O(n logn) 
# it uses extra arrays but not sure if that would be O(n)
def mergeSort(arr):
  #base condition
  if len(arr) > 1:
    #mid
    mid = len(arr)//2
    #left and right arrays
    l = arr[:mid]
    r = arr[mid:]
    #sorting first and second half
    mergeSort(l)
    mergeSort(r)

    i = j = k = 0

    #copying data to the arrays
    while i < len(l) and j < len(r):
      if l[i] < r[j]:
        arr[k] = l[i]
        i+=1
      else:
        arr[k] = r[j]
        j+=1
      k+=1
    # checking if there is any element left
    while i < len(l):
      arr[k] = l[i]
      i += 1
      k += 1
    
    while j < len(r):
      arr[k] = r[j]
      j += 1
      k += 1      
  
  #write your code here
  
# Code to print the list 
def printList(arr):
  for i in range(len(arr)):
    print(arr[i], end=' ')

    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is")  
    printList(arr) 
    mergeSort(arr) 
    print("\nSorted array is: ") 
    printList(arr) 
