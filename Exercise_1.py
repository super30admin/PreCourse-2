# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
"""
Space Complexity : O(1) we are using only variables like start, mid, end
Time Complexity: Best O(1), Worst: O(log n)
"""
def binarySearch(arr, l, r, x): 
    start = l
    end = r
    target = x
    #If len(arr) is 0 it wont enter into while loop and directly prints -1
    #if len > 1 we enter into the while loop to find the index of the target
    while(start<=end):
      mid = (start + end) //2
      #if arr[mid] == target we return the index
      if arr[mid] == target:
          return mid
      #if arr[mid] < target that means the target may present after the midpoint. so we need to search in those indexes.
      elif arr[mid] < target:
          start = mid + 1
      #if arr[mid] > target that means the target may present after the midpoint. so we need to search in those indexes.
      else:
          end = mid - 1
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
