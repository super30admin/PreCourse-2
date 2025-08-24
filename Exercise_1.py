# Python code to implement iterative Binary  
# Search. 

# // Time Complexity : O(logn)
# // Space Complexity : O(1) saving the index in index variable 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  # assuming the given array is a sorted array 
  # binary search is usualy performed on sorted arrays, and since we know its sorted and given a value it will be in range left < value < right so once we found the 
  # mid of the array and its value is greater than the value we are looking for, no need to look for the right half since all those values
  # will be greater than the x so update the right as mid -1 (we already checked mid why to check again and also if we equate left and right to mid it will go on infinte loop)
  # same with left variable once the value of mid is less than x then  left half all the values will be less than x, no need to iterate the left half
  # updte the left = mid +1
  # iterate the loop to find the index if not found return -1 


  index = -1 # if index found retun the index if ot return -1 so saving the index with -1

  while ( l <= r):
      mid = (l+r)//2
      if arr[mid] == x:
          index = mid
          return index # once found updating the index 
      elif arr[mid] > x :
          r = mid -1
      else :
          l = mid + 1

  return index
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 12
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
