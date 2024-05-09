# Python program for implementation of MergeSort 

# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

def mergeSort(arr):
  #write your code here
  if(len(arr) == 0):
      return
  if len(arr) > 1:
      # Midpoint of array
      mid = len(arr) // 2
      # Dividing the array elements into 2 halves
      left = arr[:mid]
      right = arr[mid:]
      # Sorting each half recursively
      mergeSort(left)
      mergeSort(right)
      # Merging the sorted halves
      i = j = k = 0
      while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
      # Checking if any element was left
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
    #write your code here
    if(len(arr) == 0):
        print("Empty array")
    for i in range(len(arr)):
        print(arr[i],end = " ")
    print("\n")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 11, 0, 0, 66, -6, 6, 7, 90,-86,-33,7878]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
