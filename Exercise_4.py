# Python program for implementation of MergeSort 

# the array is divided into halves using recursion until it cannot be further divided
# once the array is divided it is merged in a sorted manner.

def merge(arr1,arr2):
  i,j = 0,0
  result = []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      result.append(arr1[i])
      i+=1
    else:
      result.append(arr2[j])
      j+=1
  while i < len(arr1):
    result.append(arr1[i])
    i+=1
  while j < len(arr2):
    result.append(arr2[j])
    j+=1
  return result
  
    
def mergeSort(arr):
  if len(arr) <=1:
    return arr
  mid = len(arr)//2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  return merge(left, right)
  
  
# Code to print the list 
def printList(arr): 
  print(arr)
    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    result = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(result) 
