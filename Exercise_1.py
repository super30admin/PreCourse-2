'''
Time and space complexity:

Time -> O(log(n))
Space -> O(1) since we don't use any extra memory other than the input array
'''


# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 

  #write your code here
  while (l <= r):
    middleIdx = (l + r)//2
    if arr[middleIdx] == x:
      return middleIdx
    elif arr[middleIdx] < x:
      l = middleIdx + 1
    else:
      r = middleIdx - 1
  return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
  print("Element is present at index % d" % result)
else: 
  print("Element is not present in array")
