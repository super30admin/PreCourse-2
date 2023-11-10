# Python program for implementation of MergeSort
# Merge Sort - O(nlogn) in all cases
# Space - O(n) - we use this to store our left and right arrays
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
      mid = len(arr)//2
      left = arr[:mid]
      right = arr[mid:]
      mergeSort(left)
      mergeSort(right)

      i= 0
      j= 0
      k = 0

      while i< len(left) and j< len(right):
          # If left array element is smaller, insert left array element first
          if left[i] < right[j]:
              arr[k] = left[i]
              i+=1
          else:
              arr[k] = right[j]
              j+=1
          k+=1
     # if there are elements still present in left array
      while i < len(left):
          arr[k] = left[i]
          i+=1
          k+=1
    # If elements are still present in the right array
      while j < len(right):
          arr[k] = right[j]
          j+=1
          k+=1


# Code to print the list 
def printList(arr): 
    for element in arr:
        print(element, end = " ")
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
