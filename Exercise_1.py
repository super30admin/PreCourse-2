# Author: Vineet Khanna
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# TC: O(log(n), as we divide the array in two repeatedly.
def binarySearch(arr, l, r, x):
  #write your code here
    middle = 0
    while l <= r:
        #calculating middle element of array.
        middle = (l+r)//2

        #Check if element is on left of middle.
        if arr[middle]>x:
            r = middle-1

        #Check if element is on right of middle.
        elif arr[middle]<x:
            l = middle+1
            
        else:
            return middle
    return -1

  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
