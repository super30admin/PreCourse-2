# 1. Python code to implement iterative Binary Search.

# It returns location of x in given array arr if present, else returns -1


# Time Complexity  : o(logn)
# Space Complexity :  o(1)
# Algorithm
'''
1. Search the list using first and last
2. if value at mid point is greater than x search the list in first half
   else second half
3. keep track of element present or not prsent using found parameter
4. if entire list is traversed return -1
'''

def binarySearch(arr, l, r, x):
    
    first=l
    last=r
    found=False
    mid =(first+last)//2
    while first<last and mid<= r and not found:
        val=arr[mid]
        
        if val==x:
            found=True
            return x
        else:
            if val<x:
                first=mid
            else:
                last=mid  
        mid=(first+last)//2
    return -1
            
            
    

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 1

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index % d" % result )
else:
    print ("Element is not present in array")