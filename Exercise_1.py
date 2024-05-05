# Python code to implement iterative Binary  # Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 

    if x < arr[l] or x > arr[r]:
      print("out of bounds")
      return -1 
    
    if r-l == 1:
      if arr[r]== x:
        print("right")
        return r 
      if arr[l]==x:
        print("left ")
        return l
    
    m = l +int((r-l)/2) ; print("index", l, m, r)
    if arr[m]==x:
      return m
    

    if arr[m]<x:
      return binarySearch(arr, m+1, r, x) 
    else:
      return binarySearch(arr, l, m-1, x)  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
# Function call 
for x in arr:
  print("\nSearch", x)
  result = binarySearch(arr, 0, len(arr)-1, x) 
  print("Result:", result)
  if result != -1: 
      print("Element is present at index % d" % result)
  else: 
      print("Element is not present in array")