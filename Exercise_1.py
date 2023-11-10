
# // Time Complexity : O(log n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :no

#  Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 




def binarySearch(arr, l, r, x): 
  while l<=r:

    middle = (l+r)//2
    if arr[middle]==x:      #check if the middle of the array is the number we are looking for
      return middle
    if arr[middle]< x:      #if the middle is less than the number, then we know its in the right side of the array
      l=middle+1
    else:
      r = middle-1          #if the middle is bigger than the number, then its on the left side 
  return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
  print ("Element is present at index % d" % result )
else: 
  print ("Element is not present in array")
