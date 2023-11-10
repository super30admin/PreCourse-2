# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:

    midpoint = len(arr) // 2
    leftArray = arr[:midpoint]
    rightArray = arr[midpoint:]

    mergeSort(leftArray)
    mergeSort(rightArray)

    i = j = k = 0

    while i < len(leftArray) and j < len(rightArray):
      if leftArray[i] < rightArray[j]:
          arr[k] = leftArray[i]
          i += 1
      else:
          arr[k] = rightArray[j]
          j += 1
      k += 1

          # Checking if any element was left
    while i < len(leftArray):
        arr[k] = leftArray[i]
        i += 1
        k += 1

    while j < len(rightArray):
        arr[k] = rightArray[j]
        j += 1
        k += 1
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
      print(arr[i], end= " ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
