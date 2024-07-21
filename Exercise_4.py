# // Time Complexity : O (nlogn)
# // Space Complexity : O(n) - recursion stack
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : made some silly mistakes to get to working code.
# missed the recursion terminating condition and incorrect variable names


# // Your code here along with comments explaining your approach
# using recursion to divide the given array into left and right arrays.
# if arr size is 1 then return the array
# if arr is greater continue to divide
# once divided merge by sorting each element into the same array
# not using any auxilliary array but recursion stack takes O(n) space

# Python program for implementation of MergeSort 
def mergeSort(arr):
    # if single element in partitioned array return it
    if len(arr) == 1:
       return arr
    
    if len(arr) > 1:
      # divide array into left and right
      left = mergeSort(arr[:len(arr)//2])
      right = mergeSort(arr[(len(arr)//2):]) 
      

      l = len(left)
      r = len(right)
      i = j = k = 0
      while ( i < l  and j < r):
        if left[i] <= right[j]:
          arr[k] = left[i]
          i += 1
        else:
          arr[k] = right[j]
          j += 1
        k += 1
      while (i < l):
         arr[k] = left[i]
         k += 1
         i += 1
      while (j < r):
         arr[k] = right[j]
         k += 1
         j += 1
      return arr
        
    
  #write your code here
  
# Code to print the list 
def printList(arr): 
  print(arr, end=" ")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
