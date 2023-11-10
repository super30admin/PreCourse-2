# Time Complexity : O(n log n) is the time
# Space Complexity :  O(n) since we use an extra array to merge
# Did this code successfully run on Leetcode : Did not try running code on leetcode as the question and inputs on leetcode are bit different.
# Any problem you faced while coding this :  No issues faced

# Your code here along with comments explaining your approach

# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
  if len(arr) > 1:
    mid = len(arr)//2                       #calculating mid
    leftArray = arr[:mid]                   #creating left subarray from start to mid - 1
    rightArray = arr[mid:]                  #creating right subArray from mid to end

    mergeSort(leftArray)                    #recursive call on left subArray
    mergeSort(rightArray)                   #recursive call on right subArray

    #implementing merge functionality
    i, j, k = 0, 0, 0                       #i, j, k are used to keep track of indexes in leftArray, rightArray and mergeArray
    while i < len(leftArray) and j < len(rightArray):
      if leftArray[i] < rightArray[j]:       #if left array value is < right array value we add the left value to the temporary array
        arr[k] = leftArray[i]                #then increment counts respectively
        i += 1
        k += 1
      else:                                   #if right array value is less than left array val then we add right value to temporary array
        arr[k] = rightArray[j]                #then increment counts respectively
        j += 1
        k += 1

    while i < len(leftArray):                 #if there are left over elements in the left array we add those remaining elements on to the 
      arr[k] = leftArray[i]                   #temporary array(final array)
      i += 1
      k += 1

    while j < len(rightArray):                #if there are remaining elements in the rightarray then we add them to final array
      arr[k] = rightArray[j]
      j += 1
      k += 1

# Code to print the list 
def printList(arr):
    #write your code here
    for i in range(len(arr)):
      print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
