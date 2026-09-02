# Python code to implement iterative Binary  
# Search. 
  
# It returns location of target in given array arr  
# if present, else returns -1 
'''
arr = [2 3 5 [10] {40}]
left = 3
right = 4
middle = 3
target = 10
'''
def binarySearch(arr, left, right, target): 
  #write your code here
  while left <= right:
    middle = (left + right) // 2

    if arr[middle] == target:
       return middle
    elif arr[middle] < target:
       left = middle + 1
    else:
       right = middle - 1

  return - 1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
target = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr) - 1, target) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
