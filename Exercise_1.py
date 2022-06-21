'''
Time Complexity : O(logn)
Space Complexity : O(1) //O(logn) if use recursion to solve binary search
'''
def binarySearch(arr, low, high, key): 
  
  #write your code here
  
  while(low<=high):
    mid = (low + high)//2
    if (arr[mid] == key):
      return mid
    elif(arr[mid]<key):
      low = mid + 1
    elif (arr[mid]>key):
      high = mid-1
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
