# Time Complexity :O(logN) 
# Space Complexity : O(1) for the worst case where N is the size of the linkedlist 
# Did this code successfully run on Leetcode : I tried in VS code 
# Any problem you faced while coding this :No

# I am iterating through the array by first finding the middle elemnent of the array then if the key is in the middle element 
# then return the mid else check if the key is smaller or larger than the mid element and then shrink the search space and 
# again check the mid
def binarySearch(arr, l, r, x): 
    while l <= r:
        mid = (l+r) // 2
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
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")