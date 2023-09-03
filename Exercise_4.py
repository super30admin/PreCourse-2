# Python program for implementation of MergeSort 
def mergeSort(arr):
  divide(arr,0,len(arr)-1)

def divide(arr,si,ei):
  if si >= ei:
    return

  mid = si + (ei-si)//2
  divide(arr,si,mid)
  divide(arr,mid+1,ei)
  conquer(arr,si,mid,ei)

def conquer(arr,si,mid,ei):
  result = []
  idx1 = si
  idx2 = mid
  x = 0
  while(arr[idx1] <=arr[mid] and arr[idx2] <= arr[ei]):
    if arr[idx1] <= arr[idx2]:
      result[x] = arr[idx1]
      x += 1
      idx1 += 1
    else:
      result[x] = arr[idx2]
      x += 1
      idx2 += 1
  while idx1 <= mid:
    result[x] = arr[idx1]
    x += 1
    idx1 += 1
  while idx2 <= ei:
    result[x] = arr[idx2]
    x += 1
    idx2 += 1

  j = 0
  for i in range(0,len(result)):
    arr[j] = result[i]
    j += 1


  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(0,len(arr)):
      print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
