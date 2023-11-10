# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#time complexity: O(log n)
#space complexity:O(1)

def binarySearch(arr, l, r, x): 
  #while we have lower bound less than to upper bound
  while l<=r:
     #get the middle of the array
    middle= (l+r)//2
    
    #if we found the value of x in the middle of array
    if arr[middle]==x:
      #return index of value
      return middle

    else:
      #if the value is greater than the value at middle, then increase lower bound
      if arr[middle]< x:
        l = middle + 1

      else:
        #else value is lesser than the value at middle, decrese upper bound 
        r = middle - 1

    #if value is not found in the array    
  return -1


# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
# Function call
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
  print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
