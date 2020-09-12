# Python program for implementation of MergeSort 
# Time Complexity: O(nlog(n))
# So merge sort works with a divide and conquer approach
# where you divide the arrays into smaller and smaller sections 
# which get sorted and then finally you merge the sorted subsections together.

def mergeSort(arr):
  
  #write your code here

  def merge(arr, l,  mid, h):
    i, j = l, mid
    tempList = []
    k = 0
    while i < mid and j < h:
      
      if arr[i] < arr[j]:
        tempList.append(arr[i])
        i += 1
      else:
        tempList.append(arr[j])
        j += 1
      k += 1

    while i < mid:
      tempList.append(arr[i])
      i += 1
    
    while j < h:
      tempList.append(arr[j])
      j += 1

    arr[l:h] = tempList

  def divide(arr, l, h):
    if h - l <= 1:
       return
    
    mid = l + (h - l) // 2

    divide(arr, l, mid)
    divide(arr, mid, h)

    merge(arr, l, mid, h)
  
  divide(arr, 0, len(arr))

  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
