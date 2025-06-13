#Time Complexity: nlogn
#Space Complexity: O(1)

# Python code to implement iterative Binary
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    while l<r:
        mid = (l + r) // 2  #find middle index each time for the range
        if arr[mid]==x:
            return mid
        elif arr[mid]>x: #check if middle value of range if greater than target, then high_index=middle-1
            r=mid-1
        elif arr[mid]<x: #check if middle value of range if lesser than target, then low_index=middle+1
            l=mid+1
    return -1


    #alternate approach
    # if l > r:
    #     return -1
    #
    # mid=(l+r)//2
    #
    # if l==r:
    #     if arr[mid] == x:
    #         return mid
    #     else:
    #         return -1
    # elif arr[mid]>=x:
    #     return binarySearch(arr,l,mid,x)
    # elif arr[mid]<x:
    #     return binarySearch(arr,mid+1,r,x)
    #
    # return -1

  #write your code here

# Test array 
arr = [ 2, 3, 4, 10, 40 ]
x = 10
arr = sorted(arr)   # sorting if input is not in sorted order
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
