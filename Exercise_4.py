# Python program for implementation of MergeSort
def mergeSort(arr):

  #write your code here
  if len(arr)>1:

      mid = len(arr)//2
      left = arr[:mid]
      right = arr[mid:]
      mergeSort(left)
      mergeSort(right)
      i=0
      j=0
      k=0
      while (j<len(left) and k <len(right)):
          if left[j]<right[k]:
              arr[i]=left[j]
              j=j+1
          else:
              arr[i]=right[k]
              k=k+1
          i=i+1
      while(j<len(left)):
          arr[i]=left[j]
          j = j+1
          i = i+1
      while (k<len(right)):
          arr[i] = right[k]
          k=k+1
          i=i+1
# Code to print the list
def printList(arr):

    #write your code here
    for i in range(len(arr)):
        print(arr[i])

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
