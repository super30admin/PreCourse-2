# Python program for implementation of MergeSort 
# Time complexity: O(n log n)
# Space complexity : O(n)

def mergeSort(arr, l, r):
  
  #write your code here
  if l < r:
    middle = l + (r-l) // 2
    left = mergeSort(arr, l, middle)
    right = mergeSort(arr, middle+1, r) 
    i, j = 0, 0
    mergeArr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
          mergeArr.append(left[i])
          i += 1
        else:
          mergeArr.append(right[j])
          j += 1
    while i < len(left):
      mergeArr.append(left[i])
      i += 1
    while j < len(right):
      mergeArr.append(right[j])
      j += 1 
    return mergeArr
  elif l == r:
     return [arr[l]]
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
