# Python program for implementation of MergeSort 

def mergeSort(arr):
  
  #write your code here

  low = 0
  high = len(arr)-1
  res = [-1]*len(arr)

  def merge(arr, low, high, mid):

    i = low
    j = mid+1
    idx = low

    while i <= mid and j <= high:
      if arr[i] <= arr[j]:
        res[idx] = arr[i]
        i += 1
      else:
        res[idx] = arr[j]
        j += 1

      idx += 1

    if i < mid:
      while i <= mid:
        res[idx] = arr[i]
        idx += 1
        i += 1

    elif j < high:
      while j <= high:
        res[idx] = arr[j]
        idx += 1
        j += 1

    return res
  
  def mergesort(arr, low, high):
      if low >= high:
        return
      
      mid = (low+high)//2

      mergesort(arr, low, mid)
      mergesort(arr, mid+1, high)
      merge(arr, low, high, mid)

  mergesort(arr, low, high)

  return res

  

    
  
#mergeSort([])
  
# Code to print the list 
def printList(arr): 
    for num in arr:
      print(num, end=' ')
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
