# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if len(arr)== 0:
    return -1
  middle =  (l+r)//2
  if x == arr[middle]:
    return middle
  else:
    if x < arr[middle]:
      return binarySearch(arr,l,(middle-1),x)
    else:
      return binarySearch(arr,(middle+1),r,x)




  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")

