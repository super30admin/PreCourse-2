# Python code to implement iterative Binary  
# Search. 
# Time Complexity : O(log(size of array))
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this :
# NO
#
# Your code here along with comments explaining your approach :
# array always needs to be sorted is one major assumption I took into consideration.
# Since its sorted and we need to find only one elment we need to narrow down our search if the mid element is not
# matching then there is no chance that the value with less that that matches.
# so we go for the side which we thing there might be one value present
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    # write your code here
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10
arr = [2]
x = 2

arr = []

arr = [2, 4]

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index ", result)
else:
    print("Element is not present in array")
