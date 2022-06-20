# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  mid = int((l+r)/2)
  if(arr[mid]==x):
    return mid
  elif(x<arr[mid]):
    for i in range(l,mid):
      if(arr[i]==x):
        return i
  else:
    for j in range(mid,r):
      if(arr[j]==x):
        return j
  return -1
  
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index {}".format(result))
else: 
    print("Element is not present in array")
