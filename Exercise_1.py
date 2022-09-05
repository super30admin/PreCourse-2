#Time Complexity - O(n log n)
#Space Complexity - o(n)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  size = len(arr)
  if size == 1:
      if arr[0] == x:
          return 0
      else:
          return -1
  else:
      mid = 0
      if size % 2 == 0:
          mid = size//2
      else:
          mid = (size+1)//2
      result = 0
      if x <= arr[mid]:
          for i in range (0,mid+1):
              if arr[i] == x:
                  result = i
                  return result
      elif x > arr[mid]:
          for i in range (mid+1,size):
              if arr[i] == x:
                  result = i
                  return result
      return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
