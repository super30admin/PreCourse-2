# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  
  if (l+r)%2==0:
    mid_idx=(l+r)//2
  else:
    mid_idx=((l+r)+1)//2
  
  print("mid index=",mid_idx, "Left=",l, "Right=", r)
  
  if l>r:
    return -1
  else:
    if x==arr[mid_idx]:
      return mid_idx
    elif(arr[mid_idx]<x):
      result1 = binarySearch(arr,mid_idx+1,r,x)     
      return result1
    elif(arr[mid_idx]>x):
      print(" mid>x", mid_idx)
      result2 = binarySearch(arr,l,mid_idx-1,x)
      print(" !! arr[mid]>item result=",result2)
      return result2

  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 50
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)
  
if result != -1: 
    print ("Element is present at index ", result )
else: 
    print ("Element is not present in array")
