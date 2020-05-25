# Time Complexity : O(log(n))
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
def iterativeBinarySearch(arr, l, r, x):
    # for every iteration eliminating half the search space by choosing
    # a mid value depending on the value of x since arr is sorted
    left = l
    right = r
    while left <= right:
        mid = left + (right - left) / 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1
    return -1

def recursiveBinarySearch(arr, l, r, x):
    if l <= r:
        mid = l + (r - l) / 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return recursiveBinarySearch(arr, l, mid-1, x)
        elif x > arr[mid]:
            return recursiveBinarySearch(arr, mid+1, r, x)
    return -1

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = iterativeBinarySearch(arr, 0, len(arr)-1, x)
result1 = recursiveBinarySearch(arr, 0, len(arr)-1, x)

if result != -1 and result1 != -1:
    print "For Iterative search element is present at index % d" % result
    print "For Recursive search element is present at index % d" % result1
else: 
    print "Element is not present in array"
