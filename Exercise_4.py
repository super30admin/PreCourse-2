#TC o(nlogn)
#SC o(n)
# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
    # divide the array into two using slicing
      left = arr[:len(arr)//2]
      right = arr[len(arr)//2:]      

      #recursively calling merge sort
      mergeSort(left)
      mergeSort(right)

      #merging
      i1 = 0 #index of left
      i2 = 0 #index of right
      i3 = 0 #index of merged

      while i1 < len(left) and i2 < len(right):
            if left[i1] < right[i2]:
              arr[i3] = left[i1]
              i1 += 1
            else:
              arr[i3] = right[i2]
              i2 += 1
            i3 += 1        
      while i1 < len(left):
            arr[i3] = left[i1]
            i1 += 1
            i3 += 1
      while i2 < len(right):
        arr[i3] = right[i2]
        i2 += 1
        i3 += 1


# Code to print the list 
def printList(arr): 
    for i in range(0,len(arr)):
          print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
