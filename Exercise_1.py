#Time Complexity = O(n logn)
#Space complexity = O(1)
#The approach for this is pretty similar where I took the length and divided the arry lenght by half and checked if middle value is less then target value or not.
#In this the target index in the sorted array os found


# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  lent = len(arr)
  middle = (l + r) // 2
  print(middle)

  while l <= r:
    if arr[middle] < x:
      print("debug if")
      l = l + 1
    elif arr[middle] == x:
      return x
    else:
      print("I came here")
      r = middle - 1
  
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
