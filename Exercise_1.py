# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):

    i=l
    j=r

    while i<=j:

        mid=i+(j-i)//2

        if arr[mid]==x:
            return i
        elif arr[mid]>x:
            j=mid-1
        else:
            i=mid+1

    return -1

# Test array
arr = [ 2 ]
x = 2

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index ",result)
else:
    print ("Element is not present in array")
