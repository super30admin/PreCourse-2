# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
from array import array


position=0


def binarySearch(array, l, r, x): 
  l=0
  r=len(array)-1
  while l<r:
    mid=(l+r)//2
    if(array)==x:
      globals()['Position']=mid
      return True
    else:
      if array[mid]<x:
        l=mid
      else:
        r=mid

  
  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
if binarySearch(array,x):
  print("Location is", position+1)
else:
  print("Not in the List")

