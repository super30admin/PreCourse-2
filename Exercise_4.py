# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  def helper(arr, left, right):
    if left<right:
      mid = (left+right)//2
      helper(arr, left, mid)
      helper(arr, mid+1, right)
      merge(arr, left, mid, right)
  
  def merge(arr, left, mid, right):
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    L.append(float('inf'))
    R.append(float('inf'))
    i=j=0

    for x in range(left, right+1):
      if L[i]<=R[j]:
        arr[x] = L[i]
        i+=1
      else:
        arr[x] = R[j]
        j+=1
      
  helper(arr, 0, len(arr)-1)
      
    
  
  
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
