# Python code to implement iterative Binary  
# Search. 
# Time Complexity : O(log n)
# Space Complexity : O(1)
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    if r>=1:
        m = int((l + (r+1))/2)
        s = arr[l]
        if arr[m]>x:

            r = m
            while l<r+1:
                if arr[l] == x:
                    return l

                l +=1

        elif arr[m]<x:
            l = m+1
            while l<r+1:
                if arr[l] == x:
                    return l

                l +=1

        elif arr[m] == x:
            return m

        if l >= r:

            return -1
  #write your code here

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 4
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
