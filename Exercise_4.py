
# Python program for implementation of MergeSort 
def merge(lArr, rArr):
  newArray = []
  l, r = 0, 0
  while l < len(lArr) and r < len(rArr):
    if lArr[l] < rArr[r]:
      newArray.append(lArr[l])
      l += 1
    else:
      newArray.append(rArr[r])
      r += 1
    
  while l < len(lArr):
    newArray.append(lArr[l])
    l += 1
  
  while r < len(rArr):
    newArray.append(rArr[r])
    r += 1
      
  return newArray

def mergeSort(l, r, arr):
  if l == r:
    return [arr[l]]
  mid = l +(r - l)//2
  lArr = mergeSort(l, mid, arr)
  rArr = mergeSort(mid + 1, r, arr)
  ret = merge(lArr, rArr)
  return ret



  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for a in arr:
      print(a)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(0, len(arr) - 1, arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
