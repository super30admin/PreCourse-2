#Time Complexity 
#Best Case ->O(1)
#Average Case ->O(log n)
#Worst case ->O(log n)
#Space complexity-> O(1)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
    mid = (l+r) // 2 #middle index
    mid_value = arr[mid]
    if mid_value == x:
      return mid  #found target return the index
    elif mid_value < x:
      l = mid + 1 #search at right half
    else:
      r = mid -1  #search at left half
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
