# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here

  # O (logn) Time Complexity | O (1) Space Complexity
  
    while (l <= r):     # continually update l or r by checking one of the 3 conditions
        mid = int((l + r) / 2)

        if (x == arr[mid]):     # return mid index if found else return -1 if l > r i.e. not found
            return mid

        elif (x < arr[mid]):
            r = mid - 1

        else:
            l = mid + 1

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
