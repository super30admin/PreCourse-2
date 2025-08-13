# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

"""
Time Complexity: O(Logn) where n = number of elements in the array
Space Complexity: O(1)

Edge cases: empty list, one element in the list, first or last element, element not present
"""
def binarySearch(arr, l, r, x): 
  #write your code here

  while l <= r:
    mid = (l + r)//2

    if x > arr[mid]:
       l = mid + 1
    elif x < arr[mid]:
       r = mid - 1
    elif x == arr[mid]:
       return mid
  return -1
  
    
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
#arr = []
#arr = [10]
#arr = [ 2, 3, 4, 10, 40 ] 
#x = 2
#arr = [ 2, 3, 4, 10, 40 ] 
#x = 40
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  

if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
