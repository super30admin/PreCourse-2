# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : log(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no
def binarySearch(arr, l, r, x): 

  #write your code here

  while l<=r:
    m = (l + r)//2

    if x == arr[m]:
      return m

    elif x < arr[m]:
      r = m - 1

    else:
      l = m + 1  


# Test array 

result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
    
    print ("Element is present at index % d" % result )
else: 
   
    print ("Element is not present in array")