# Time Complexity : O(nlogn)
# Space Complexity : O(1)

# Python program for implementation of MergeSort 
def merge(arr, l, m, h):
  left = arr[l:m+1]
  right = arr[m+1:h+1]
  i, j, k = l, 0, 0
  while j < len(left) and k < len(right):
    if left[j] <= right[k]:
      arr[i] = left[j]
      j += 1
    else:
      arr[i] = right[k]
      k += 1
    i += 1
  
  while j < len(left):
    arr[i] = left[j]
    j += 1
    i += 1
  
  while k < len(right):
    arr[i] = right[k]
    k += 1
    i += 1


def mergeSort(arr, l, h):
  
  #write your code here
    if (l<h):
      mid = (l+h)//2
      mergeSort(arr, l, mid)
      mergeSort(arr,mid+1,h)
      merge(arr, l,mid,h)

# Code to print the list 
def printList(arr):   
  #write your code here
  print(arr)


# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
