# Python code to implement iterative Binary Search. 
# // Time Complexity : O(log N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Needed to go through algorithm


# // Your code here along with comments explaining your approach

# It returns location of x in given array arr  
# if present, else returns -1 

#Used recursion and kept iterating on small sub arrays formed with the help of mid
#Sorted Array in ascending order
def binarySearch(arr, l, r, x): 
	result = -1
    if r >= l:
        mid = (l+r)//2
        if (arr[mid]==x):
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return result



# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
print "Element is present at index % d" % result 
else: 
print "Element is not present in array"
