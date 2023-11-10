#time complexity: O(logn) 
#space complexity: O(1)

#time complexity explanation: as we use divide and conquer method, we'll search the array by dividing it by two repeatedly until we find the x 
# n => n/2 -> n/4 ->n/8 ->.....->1 
# 2^x ~ n 
# x ~ log2 n 
# O(log2 n) = O (logn)  

#space complexity explanation: In an iterative implementation of Binary Search, the space complexity will be O(1). This is because we need two variable to keep track of the range of elements that are to be checked. No other data is needed


def binarySearch(arr, l, r, x): 
    while l<=r: 
      mid  = (l+r)//2 

      if arr[mid] == x: 
        return mid  
      elif arr[mid]>x: 
        r = mid-1 
      else: 
        l = mid+1  
    return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 50
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result)
else: 
    print ("Element is not present in array")
