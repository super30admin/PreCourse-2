# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : I came up with the merge function with extra space using result array
#                           But I wanted to merge inplace since that would be efficient, came to know about
#                           Gap method but didn't spend too much time there and marked as a algorithm to learn
#                           once I am done with week 4 since it was difficult to understand.


# Python program for implementation of MergeSort
def mergeSort(arr, l, h):
  
  #write your code here
  '''
  If the array is of length 1, do nothing.
  Find a midpoint and call mergeSort on both left and right parts of midpoint.
  merge both the left and right parts once they are sorted individually.
  '''
  if l == h:
     return
  m = l + (h-l) // 2

  mergeSort(arr, l, m)
  if m+1 < h:
    mergeSort(arr, m+1, h)
  merge(arr, l, m, h)

def merge(arr, l, m, h):
  '''
  i goes through the left part of the array
  j goes through the right part of the array

  We choose the smallest number from both the parts and add it to the results array
  once any one part is fully added in the result array, we add the rest of the elements to result

  Finally we put the sorted array result into the appropriate place in the arr array.
  '''
  i = l
  j = m+1
  result = []

  while i <= m and j <= h:
    if arr[i] <= arr[j]:
      result.append(arr[i])
      i+=1
    else:
      result.append(arr[j])
      j+=1

  if i <= m:
     for x in arr[i:m+1]:
       result.append(x)

  if j <= h:
     for x in arr[j:h+1]:
       result.append(x) 

  for i in range(len(result)):
     arr[l+i] = result[i]
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
