# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:

    #Find mid of array
    mid = len(arr) // 2

    #get the left half
    left = arr[:mid]
    #get the right half
    right = arr[mid:]

    #sort each half
    mergeSort(left)
    mergeSort(right)

    i=j=k=0
    # merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    #Check if any element is left in any of the halves and add to the array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
 
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

  
# Code to print the list 
def printList(arr): 
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
