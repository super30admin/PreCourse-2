# Python code to implement iterative Binary  
# Search. 
# Time Complexity : O(log n)
#  Space Complexity : O(log n)
# Did this code successfully run on Leetcode : Yes

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr1, r, l, x):
    # write your code here
    med = r+(l-r)// 2
    if arr1[med] == x:
        return med
    elif arr1[med] < x:
        return binarySearch(arr1, med + 1, l, x)
    elif arr1[med] > x:
        return binarySearch(arr1, 0, med - 1, x)
    else:
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr) - 1, x)
print(result)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
