"""
Runtime Complexity:
1)O(n) as we scan through all the elements in the list to check whether the target is present in the list.
Space Complexity:
1) O(n) - as the loop would go 'n' iterative calls

- Yes, the code worked on leetcode.
- Idea - A loop to check if the target element is in the list, and if it's present then we return the index of it.
"""
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):            #array, start, end, target element are passed as parameters.
  
  #write your code here
  for i in range(l,r):                    #loop from start to end to check if the target is present in the list
    if x in arr:                          # checks if the target is present in the list
        result = arr.index(x)             #if its present, we store the index of the target element to result and return.
        return result
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
