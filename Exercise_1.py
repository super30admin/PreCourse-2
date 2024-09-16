# Python code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):

    first=l
    last=r
    found=False

    mid=(first+last)//2
    while first<=last and not found:
        val=arr[mid]
        if x==val:
            return mid
        else:
            if x > val:
                first=mid+1
            else:
                last=mid-1
        mid=(first+last)//2

    return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("Element is present at index % d" % result )
else:
    print ("Element is not present in array")
