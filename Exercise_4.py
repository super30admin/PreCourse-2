# Time Complexity : Merging two array of size n has a time complexity of O(n) and we divide the array log n time. Hence over time complexity is O(nlogn)
# Space Complexity : 
# Any problem you faced while coding this : Having sifficulty in understanding the space complexity of the code

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  if len(arr) > 1:
    mid = len(arr)//2 #Finding the middle index
    #Partitioning the array into 2 halves
    left = arr[:mid] 
    right = arr[mid:]
  
    #Recursively sorting both the halves of the array
    mergeSort(left)
    mergeSort(right)

    #Merging both the sorted halves
    i = j = k = 0 #Initialize pointers for left, right and arr
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1

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
