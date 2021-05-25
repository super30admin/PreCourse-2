# Python program for implementation of MergeSort 
def mergeSort(arr):

    # TODO:
    #     Time Complexity = Big O(NlogN) // divide and conquer
    #     Space Complexity = Big O(N) // takes extra space as it copies into a new array


  if len(arr)>1: # base case
      left = arr[:len(arr)//2]
      right = arr[len(arr)//2:]

      #recurse
      mergeSort(left)
      mergeSort(right)

      #merge
      i,j,k = 0,0,0 # left, right and merge indexes
      while i<len(left) and j<len(right):
          if left[i] < right[j]:
              arr[k] = left[i]
              i+=1
          else:
              arr[k] = right[j]
              j+=1
          k+=1

      # case when right array elements are merged, but left array elements are pending
      while i<len(left):
         arr[k] = left[i]
         i+=1
         k+=1

      # case when left array elements are merged, but left right elements are pending
      while j < len(right):
          arr[k] = right[j]
          j+=1
          k+=1





  #write your code here

# Code to print the list
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
