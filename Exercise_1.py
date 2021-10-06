# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, low, high, x):
  low=0
  high=len(arr)-1
  while(low<=high):
    mid=(high+low)//2

    if(x<arr[mid]):
      high=mid-1
    
    elif(x>arr[mid]):
      low=mid+1

    elif(x==arr[mid]):
      return mid
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index: ",result)
else: 
    print("Element not present in the array")
