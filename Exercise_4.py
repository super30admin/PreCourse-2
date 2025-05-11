# Python program for implementation of MergeSort 
def mergeSort(arr):
    
    if len(arr) > 1:
      return mergeSortHelper(arr,0,len(arr) - 1)
  
  #write your code here

def mergeSortHelper(arr,low,high):
    if low == high:
        return [arr[low]]
    mid = (low+high) // 2
    arr1 = mergeSortHelper(arr,low,mid)
    arr2 = mergeSortHelper(arr,mid+1,high)
    return divideconquer(arr1,arr2)

def divideconquer(arr1,arr2):
    i,j=0,0
    sortedarray=[]
    while i< len(arr1) and j< len(arr2):
        if arr1[i] < arr2[j]:
          sortedarray.append(arr1[i])
          i+=1
        else:
          sortedarray.append(arr2[j])
          j+=1
    while i < len(arr1):
      sortedarray.append(arr1[i])
      i += 1
    while j < len(arr2):
      sortedarray.append(arr2[j])
      j += 1

    return sortedarray
            
  
# Code to print the list 
def printList(arr): 
    for i in range(0,len(arr)):
       print(f"{arr[i]}, ", end=" ")
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr1 = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr1)