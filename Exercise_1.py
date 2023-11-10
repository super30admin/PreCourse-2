#Space complexity is O(1)
#Time complexity is O(log n), where n is the number of elements in array since at each iteration the range is halved.
#Code ran successfully in leetcode terminal
#I didnot face any problem while coding this program
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
  #while runs only until l is less than or equal to r
  while(l<=r):
    #finding the mid value 
    mid=(l+r)//2
    #if the value present at the mid position is equal to x, we will return mid
    if(arr[mid]==x):
       return mid
    #if x is less than arr[mid], we will assign r value to mid-1
    elif(x<arr[mid]):
       r=mid-1
    #if x is greater than arr[mid], we will assign l value to mid+1
    else:
       l=mid+1
  #if x is not present in the array, we return -1
  return -1  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1:
  print("Element is present at index % d" % result) 
else:
  print("Element is not present in array")
