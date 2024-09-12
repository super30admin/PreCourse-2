# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1


#time complexity = o(log n ) because you are dividing the array
#iterative
def binarySearch(arr, l, h, x):
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==x:
            return mid
        #if the target is lesser than the middle element, we bring down the high pointer
        elif arr[mid]>x:
            h=mid-1
        # if the target is bigger than the middle element, we increase the high pointer
        else:
            l=mid+1
    return -1

##recursive
def binarySearch(arr, l, h, x):
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,l,mid-1,x)
        else:
            return binarySearch(arr, mid+1, h, x)
    return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ] 
x = 0
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
