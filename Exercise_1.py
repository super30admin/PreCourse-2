# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#We have assumed that the input array would be in an ascending order
def binarySearch(arr, l, r, x): 
  
  #write your code here
  if l==r:
     return l if arr[l] == x else -1
  elif  x == arr[(l+r)//2]:
     return ((l+r)//2)
  elif x<arr[(l+r)//2]:
     return binarySearch(arr,l,((l+r)//2)-1,x)
  elif x>arr[(l+r)//2]:
     return binarySearch(arr,((l+r)//2)+1,r,x)
  
  
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
