# Python program for implementation of MergeSort 


# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
def mergeSort(arr):
  
  #write your code here
  
  #Check if the length is greater than or equal to 2
  if len(arr) >= 2:
      #Find middle element
      mid=(len(arr))//2
      
      #split into two halves (temporary arrays)
      left=arr[:mid]
      right=arr[mid:]
      
      #Sort left and the right part respectively
      mergeSort(left)
      mergeSort(right)
      
      i=0
      j=0
      k=0
      
      #Merg
      while i < len(left) and j < len(right):
          if left[i] < right[j]:
              arr[k]=left[i]
              i+=1
          else:
              arr[k]=right[j]
              j+=1
          k+=1
      
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
        print(arr[i])
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
