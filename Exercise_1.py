# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  if r<l:
    return -1

  mid_index=(l+r)//2
  mid_num=arr[mid_index]

  if mid_num==x:
      return mid_index

  if mid_num<x:
      l=mid_index+1
  else:
      r=mid_index-1

  binarySearch(arr, l, r, x)
  
if __name__== '__main__':

  # Test array 
  arr = [ 2, 3, 4, 10, 40 ] 
  x = 50
  
  # Function call 
  result = binarySearch(arr, 0, len(arr)-1, x) 
  
  if result != -1: 
    print ("Element is present at index {result}") 
  else: 
    print ("Element is not present in array")
