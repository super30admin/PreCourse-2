# Python program for implementation of MergeSort 
def merge(left_sub, right_sub):
  i = j = 0
  merged = []
  while i < len(left_sub) and j < len(right_sub):
    if left_sub[i] < right_sub[j]:
      merged.append(left_sub[i])
      i += 1
    else:
      merged.append(right_sub[j])
      j += 1

  while i < len(left_sub):
    merged.append(left_sub[i])
    i += 1
  while j < len(right_sub):
    merged.append(right_sub[j])
    j += 1
  return merged

def mergeSort(arr):

  #write your code here
  if not arr: return arr
  l, r = 0, len(arr)-1
  if l == r:
    return arr
  left_sub = mergeSort(arr[:(r+l)//2 + 1])
  right_sub = mergeSort(arr[(r+l)//2 + 1:])
  arr = merge(left_sub, right_sub)
  return arr

# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(" ".join([str(i) for i in arr]))
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

'''
Time complexity: O(NlogN)
Space complexity: O(N)
'''