# Python program for implementation of MergeSort 

# Overall complexity: 
# Bestcase: O(nlogn)
# Worst case: O(nlogn)
# Average case: O(nlogn)
def mergeSort(arr):
  #write your code here
  a = b = c = 0
  # if the length of array is greater than 1 then
  if len(arr) > 1:
    # find the mid point of the array
    middle = len(arr)//2
    # partition the array into two halves
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    # sort the two array recursively until one element is left(i.e sorted array)
    mergeSort(left_arr)
    mergeSort(right_arr)

    # check if the a and b are less than the length of left and right array respectively
    while a < len(left_arr) and b < len(right_arr):
      # if the element in left array is less than the element in the right array then
      if left_arr[a] < right_arr[b]:
        # update the left array element at c position in array
        arr[c] = left_arr[a]
        # increment a by 1
        a += 1
      # if the element in left array is greater than the element in the right array then
      else:
        # update the right array element at c position in array
        arr[c] = right_arr[b]
        # increment b by 1
        b += 1
      # increment c by 1
      c += 1
    # check if all the elements in both left and right arrays are visited atleast once
    while a < len(left_arr):
      arr[c] = left_arr[a]
      a += 1
      c += 1
    
    while b < len(right_arr):
      arr[c] = right_arr[b]
      b += 1
      c += 1
  # if the length of array is less than 1 then return the array
  else:
    return arr

# Code to print the list 
def printList(arr): 
    for i in arr:
      print(i)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
