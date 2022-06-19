# Python program for implementation of MergeSort 
# time complexity: O(n logn)

#approach: divide the elements into two halves each time until all the elements are separated into single array
# then merge from bottom with mergesort_list function in a sorted manner
def mergeSort(arr):
  if(len(arr)==1):
    return arr
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  mergeSort(left)
  mergeSort(right)
  mergesort_list(left, right, arr)
  
  
  #write your code here
  
def mergesort_list(list1, list2, arr):
  i, j, k = 0, 0, 0
  while i<len(list1) and j < len(list2):
    if list1[i]<=list2[j]:
      arr[k] = list1[i]
      i += 1
    else:
      arr[k]= list2[j]
      j += 1
    k += 1

  while i < len(list1):
    arr[k]=list1[i]
    i += 1
    k += 1
  while j < len(list2):
    arr[k]=list2[j]
    j += 1
    k += 1



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
