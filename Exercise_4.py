# PreCourse_2: Exercise_4: Python program for implementation of MergeSort 

def mergeSort(arr):
  print ("Splitting of the array: ", arr)
  if len(arr) > 1:
    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righhalf = arr[mid:]
    
    #splitting the array until it is an array of single element or an empty array
    mergeSort(lefthalf)
    mergeSort(righhalf)

    i=0; j=0; k=0

    while i < len(lefthalf) and j < len(righhalf):
      if lefthalf[i] < righhalf[j]:
        arr[k] = lefthalf[i]
        i += 1
      else:
        arr[k] = righhalf[j]
        j += 1
      k += 1

    while i < len(lefthalf):
      arr[k] = lefthalf[i]
      i += 1
      k += 1

    while j < len(righhalf):
      arr[k] = righhalf[j]
      j += 1
      k += 1
  
  print("Merging", arr)

  
# Code to print the list 
def printList(arr): 
  print (arr)
    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
