#Time complexity is O(nlogn)
#Space complexity is O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) <= 1:
    return

  mid = len(arr)//2
  #write your code here
  leftarr = arr[:mid]
  rightarr = arr[mid:]
  mergeSort(leftarr)
  mergeSort(rightarr)

  i = j = k = 0
  while i < len(leftarr) and j < len(rightarr):
    if leftarr[i] > rightarr[j]:
      arr[k] = rightarr[j]
      j+=1
    else:
      arr[k] = leftarr[i]
      i+=1
    k+=1
  # check for leftout elements in arr

  while i < len(leftarr):
    arr[k] = leftarr[i]
    k+=1
    i+=1
  while j < len(rightarr):
    arr[k] = rightarr[j]
    k+=1
    j+=1


  
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
