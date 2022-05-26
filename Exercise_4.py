# Python program for implementation of MergeSort 
def mergeSort(arr):

  
  #write your code here
  if len(arr) > 1:

    mid = len(arr)//2

    Left = arr[:mid]
    Right = arr[mid:]

    mergeSort(Left)
    mergeSort(Right)

    i = 0
    j = 0
    k = 0

    size_L = len(Left)
    size_R = len(Right)

    while i < size_L and j < size_R:
      if Left[i] < Right[j]:
        arr[k] = Left[i]
        i += 1
      else:
        arr[k] = Right[j]
        j += 1
      k += 1

    while i < size_L:
      arr[k] = Left[i]
      i += 1
      k += 1

    while j < size_R:
      arr[k] = Right[j]
      j += 1
      k += 1

def printList(arr):
  size = len(arr)
  for i in range(size):
    print(arr[i], " ")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
