# Python program for implementation of MergeSort 
def mergeSort(arr):
      if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        # Recursively call mergeSort() on each half
        mergeSort(leftArr)
        mergeSort(rightArr)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
  for i in range(len(arr)):
        print(arr[i])
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


