# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  """
  check whether the right pointer is greater than equal to the left pointer
  set middle  as (left + right) // 2 or left + (right-left) // 2. Prefer using the second one because if the list is too long, left + right > max int.
  check whether the middle elemnet is equal to the the target value, if yes return it.
  else if  it is greater than the target value, than check in the first half
  else check in the second half
  if right pointer becomes less than left, return -1

  Time Complexity: O(log(n))
  Space Complexity: O(1)
  """ 
  if r >= l:
    middle = l + (r-l) //2
    if arr[middle] == x:
      return middle
    elif (arr[middle]>x):
      return binarySearch(arr, l, middle-1, x)
    elif (arr[middle < x]):
      return binarySearch(arr, middle+1, r, x)
  else:
    return -1

  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)
  
if result != -1: 
    print("Element is present at index % d" % result )
else: 
    print("Element is not present in array")
