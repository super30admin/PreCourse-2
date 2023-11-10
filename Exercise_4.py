# Python program for implementation of MergeSort 
#time complexity (O(logn))
#space complexit (O(n)) => due to the extra space taken by left and right arrays


def mergeSort(arr):
  #for mergesort we sort the left half, sort the right half and then merge those two half.
  # to do that, we divide the arrays into two halfs by getting the mid point
  # say we have an array of 4 elements, first 2 are in left array , second 2 are in Right array
  # now we have 4 seperate arrays. Coming to just the left side, in the end we still have two seperate arrays of left and right
  # let us start combining them
  # we can do that by having three pointers i, j, k.
  # i will track left, j will track right and k will be values we will replace in our original array
  # we then keep looping the left, right arrays to check for smaller element add it to new array with pointer k

  if len(arr) > 1:
    mid = len(arr) // 2

    left_array = arr[:mid]
    right_array = arr[mid:]

    mergeSort(left_array)
    mergeSort(right_array)

    i,j,k = 0,0,0


    while i < len(left_array) and j < len(right_array):
      if(left_array[i] <= right_array[j]):
        arr[k] = left_array[i]
        i += 1
      else:
        arr[k] = right_array[j]
        j  += 1
      k += 1

    
    #just adding the rest of the elements of the longer array
    #we just simply add it, because the recursion will ensure the remaining array is already sorted
    while i < len(left_array):
      arr[k] = left_array[i]
      i += 1
      k += 1

    while j < len(right_array):
      arr[j] = right_array[j]
      j += 1
      k += 1


  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    
    for value in arr:
      print(value, end=" ")
    print("\n")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
