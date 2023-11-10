# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#time complexity:O(logn)
#space complexity: O(k) where k is constant variable mid
#passed all cases on LeetCode: yes
#difficulty faced: trying to come with condition of while loop
# comments:



def binarySearch(arr, l, r, x): 
  
  #write your code here
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
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