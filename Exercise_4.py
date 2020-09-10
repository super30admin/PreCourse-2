# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)<=1:
    return arr
  mid = int(len(arr)/2)
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  return merge(left,right)

def merge(left,right):
  result = []
  i = 0
  j = 0
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
  
  result.extend(left[:i])

  result.extend(right[:j])
    
  return result
  
  
  #write your code here
  
# Code to print the list 
def printList(arr):
  for i in range(len(arr)):
    print(arr[i], end =" ") 
  print() 
  
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
