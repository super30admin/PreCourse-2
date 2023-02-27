# Python program for implementation of MergeSort 
def mergeSort(arr):
    if (len(arr) > 1):
        mid = len(arr)//2
        leftArray  = arr[:mid]
        rightArray = arr[mid:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0

        while (i < len(leftArray) and j < len(rightArray)):
            if (leftArray[i] < rightArray[j]):
              arr[k] = leftArray[i]
              i += 1
            else:
              arr[k] = rightArray[j]
              j += 1
            k += 1

        while (i <len(leftArray)):
           arr[k] = leftArray[i]
           i += 1
           k += 1
        while (j <len(rightArray)):
           arr[k] = rightArray[j]
           j += 1
           k += 1
  
# Code to print the list 
def printList(arr): 
   for i in range(len(arr)):
      print(arr[i], end = " ")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
