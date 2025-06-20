# Python code to implement iterative Binary  
# Search. 

# Time Complexity : O(logn)
# Space Complexity :O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :
#Lets use floor division in constructing it as it will be a problem for float and int in python


# Your code here along with comments explaining your approach

  
# It returns location of x in given array arr  
# if present, else returns -1

def IsAscArray(arr, highindex): #checking function if the array is in ascending order or not 
  for i in range(0, highindex):
    if arr[i] > arr[i+1]:
      return -3
  return 0
    

 

def binarySearch(arr, l, r, x):  #binary search for ascending order array
  if l <= r:
    mid = l + ((r - l)//2) #Lets use floor division in constructing it as it will be a problem for float and int in python
    if arr[mid] == x:#checking if mid is equal to x
       return mid 
    elif arr[mid] > x:
       return binarySearch(arr, l, mid-1, x) #if mid > x check left array 
    else:
       return binarySearch(arr, mid+1, r, x) # if mid < x check right array 
    return -1
  else:
     print("Input parametes are wrong\n")
     return -2
  

  #write your code here
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40]
x = 10
  
# Function call 

if IsAscArray(arr, len(arr) -1) != -3:  
  result = binarySearch(arr, 0, len(arr)-1, x)    
  if result != -1: 
      print ("Element is present at index % d" % result )
  else: 
      print ("Element is not present in array")
else:
    print("array is not sorted in ascending order")
