# Time complexity : O(nlogn)
# Space complexity : O(n)
# Did this code successfully run on Leetcode : - 


# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  n = len(arr)
  if n == 1:
    return arr

  m = n // 2
  L = mergeSort(arr[:m])
  R = mergeSort(arr[m:])

  return combine(L, R)
  
# Code to print the list 
def combine(L, R):
  result = []
  i = j = 0

  while i < len(L) and j < len(R):
    if L[i] < R[j]:
      result.append(L[i])
      i += 1
    else:
      result.append(R[j])
      j += 1
  
  result.extend(L[i:])
  result.extend(R[j:])
  return result

def printList(arr): 
    
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    sorted_array = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(sorted_array) 
