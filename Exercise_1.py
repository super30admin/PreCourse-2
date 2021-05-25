# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1

# TODO:
#     Time Complexity = Big O(log N)
#     Space Complexity = Big O(1)

def binarySearch(arr, l, r, x):
    while(l<=r):
        mid = int((l+r)/2)
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1

  #write your code here
  
    
if __name__ == '__main__':
# Test array 
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)

    if result != -1:
        print ("Element is present at index % d" % result)
    else:
        print ("Element is not present in array")
