# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
    arr.sort() #sort the array
    if len(arr) ==0: #base case
        return -1
    while(l<=r): #iterative approach
        mid = (l+r)//2
        #print(mid)
        if arr[mid]==x:
            return mid
        elif arr[mid] > x: #move right pointer
            r = mid-1
        else:
            l = mid+1 #move left pointer
    return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")

#Time Complexity:
#O(1)
