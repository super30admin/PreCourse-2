#Time complexity:O(log(n))
#space complexity: O(1)
#Ran in leetcode: yes
#problems/issues: None
#The program will return the index of first occurence of a number. Since the array is sorted, in each iteration we can 
# reduce the search space by half.
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
#from sklearn.covariance import MinCovDet


def binarySearch(arr, l, r, x): 
  
  #write your code here
  #h=r
  while(l<r):
    m=l+(r-l)//2
    if(arr[m]<x):
      l=m+1
    else:
      r=m
  return l
  

  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)  
if arr[result]==x: 
    print ("Element is present at index " + str(result)) 
else: 
    print ("Element is not present in array")
