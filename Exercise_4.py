# Time Complexity : O(n logn) since halving the elements gives us O(log n) time and we do this n times.
# Space Complexity : O(n) extra space is used for the merged_arr. Even considering that, the overall space complexity is O(n)
# Did this code successfully run on Leetcode : Code ran successfully.
# Any problem you faced while coding this : No problems

# Python program for implementation of MergeSort
def merge(left,right):
  # Function to merge left and right sides
  merged_arr = [] # Create new array to store the merged result 
  i = 0 # Index to traverse left
  j = 0 # Index to traverse right
  while(i < len(left) and j < len(right)):
    if left[i]<right[j]:
      merged_arr.append(left[i])
      i+=1
    else:
      merged_arr.append(right[j])
      j+=1
  if i < len(left):
    for x in range(i,len(left)):
      merged_arr.append(left[x])
  if j < len(right):
    for x in range(j,len(right)):
      merged_arr.append(right[x])
  return merged_arr

def mergeSort(arr):
  
  #write your code here
  if len(arr) < 2:
    return arr # Return if length of array is less than 2. Termination condition to break out of recursion
  mid = len(arr) // 2 # Find middle index
  left = mergeSort(arr[:mid]) # Apply merge sort recursively to the left half of mid
  right = mergeSort(arr[mid:]) # Apply merge sort recursively to the left half of mid
  
  return merge(left,right) # Return the merge of left and right
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
      print(i) # Print each element in the list
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) # Merge sort is not an in place sort. So, I am assigning the result of merge sort back to arr so that we can display the sorted array  
    print("Sorted array is: ", end="\n") 
    printList(arr) 
