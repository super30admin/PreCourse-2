# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1

def binarySearch(arr, l, r, x): # Iterative approach Time Complexity: O(log n) Space Complexity: O(1)
    while l <= r:
        mid = l + ((r-l) // 2)
        if x < arr[mid]:
            r = mid - 1
        elif x > arr[mid]:
            l = mid + 1
        else:

            return mid
    return -1
  #write your code here
  
# def binarySearch(arr, l, r, x): # Recursive approach Time Complexity: O(log n) Space Complexity: O(1)
#     if l <= r:
#         mid = l + ((r-l) // 2)
#         if x < arr[mid]:
#             return binarySearch(arr, l, mid - 1, x)
#         elif x > arr[mid]:
#             return binarySearch(arr, mid + 1, r, x)
#         else:
#             return mid
#     else:
#         return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 3
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x)
print(result)
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
