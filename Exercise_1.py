# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
#time complexity O(log n)
#space complexity O(1)

def binarySearch(arr, l, r, x): 

  
 if r >= l:
        mid = l + (r - l) // 2

        # here the element is present at the middle
        if arr[mid] == x:
            return mid

        # the element is smaller than the middle, then it can only be present in the left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present in the right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

 else:
        # the element is not present in the array
   return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in the array")
