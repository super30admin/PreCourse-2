# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

'''
Time Complexity 
O(logn) since we are dividing the array and searching

Space Complexity
O(logn) if using a recursive appraoch

Approach
Since the array is sorted so check the mid element if arr[mid]>value then explore left side else explore the right side
'''
def binarySearch(arr, l, r, x): 
    if l>r:
        return -1
    mid = (l+r)//2
    if arr[mid]==x:
        return mid
    elif arr[mid]>x:
        return binarySearch(arr, l, mid-1, x)
    else:
        return binarySearch(arr, mid+1, r, x)

  
  #write your code here

  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 41
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")