# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if (len(arr) > 1):
    # calculate of middle of the arr
    middle = len(arr) // 2
    # create left array with elements till middle
    leftArr = arr[:middle]
     # create right array with elements from middle till end
    rightArr = arr[middle:]

    # recursive call for left and right sub array
    mergeSort(leftArr)
    mergeSort(rightArr)

    i = j = k = 0
    # loop till we reach at the end of the left and right sub array 
    while ((i < len(leftArr)) and (j < len(rightArr))):
      # check the elements at i and j of left and right sub-array respectively. 
      if (leftArr[i] < rightArr[j]):
        # store element of left array if it is smaller in arr at k position and increment i pointer
        arr[k] = leftArr[i]
        i += 1
      else:
         # store element of right array if it is smaller in arr at k position and increment j pointer
        arr[k] = rightArr[j]
        j += 1
      k += 1
    # if there are elements in left array left then store in arr 
    while (i < len(leftArr)):
      arr[k] = leftArr[i]
      i += 1
      k += 1
     # if there are elements in right array left then store in arr 
    while (j < len(rightArr)):
      arr[k] = rightArr[j]
      j += 1
      k += 1
  
# Code to print the list 
def printList(arr):    
    #write your code here
    for i in range(len(arr)):
      print(arr[i], end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
