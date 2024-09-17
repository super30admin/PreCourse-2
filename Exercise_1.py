# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
    mid = ((r-l)//2)+l
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        #go left
        r = mid-1
    else:
        #got right
        l = mid+1

  return -1
  
    
  
# Test array 
arr = [ 2, 3, 4 ] 
x =50 
# Function call 
arr1 = [ 2, 3, 4 ] 
x1 =0 
arr2 = [ 2, 3, 4 ] 
x2 =2 

arr3 = [ 2, 3, 4 ] 
x3 =3 
arr4 = [ 2, 3, 4 ] 
x4 =3 
arr5 = [ 2, 3, 4 ] 
x5 =4 
test = [[arr,x],[arr1,x1],[arr2,x2],[arr3,x3],[arr4,x4],[arr5,x5]]
for arr,x in test:
    
    result = binarySearch(arr, 0, len(arr)-1, x) 
      
    if result != -1: 
        print("Element is present at index % d" % result)
    else: 
        print ("Element is not present in array")
