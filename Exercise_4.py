# Python program for implementation of MergeSort 
#time complexity: O(nlogn)
def mergeSort(arr):
  
  #write your code here
  #divide the whole arr into left half and right half
  if len(arr) > 1:
    mid = len(arr) // 2
    leftArr= arr[:mid]
    rightArr = arr[mid:]

    mergeSort(leftArr)
    mergeSort(rightArr)

    #merge part:
    i = 0 #index for left array
    j = 0 #index for right array
    k = 0 #index for merged array 

    while i < len(leftArr) and j < len(rightArr):
      if leftArr[i] < rightArr[j]:
        arr[k] = leftArr[i]
        i += 1
        k += 1
      else:
        arr[k] = rightArr[j]
        j += 1
        k += 1

    #check if all the elements in the merged array

    while i < len(leftArr):
      arr[k] = leftArr[i]
      i += 1
      k += 1

    while j < len(rightArr):
      arr[k] = rightArr[j]
      j += 1
      k += 1

   




  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(0, len(arr)):
      print(arr[i])


  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


#left side: l = 12  r = 11
#merge part: i = 0, j= 0, k = 0
#l [0] > r[0]  
#arr[k] = r[0]; j++; j = 1; k++; k =1;i= 0
#arr =  [11]
#check missing:
#i < len(l); arr[k] = l[i]; arr[1] = l[0]
#arr = [11, 12]

