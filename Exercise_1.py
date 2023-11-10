# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here      
  # l = left, r = right
  # calculate the middle element and check if the elem to be found is equal to mid, if yes retrn its index
  # else -> if the middle ele is greater than elem to be found, then break the array into half, move right pointer to mid-1 and serach in the new shortened array now
  # else -> if its greater, then make left pointer to new left position which is mid+1
  # continue the above steps until last element in the array and left index is less than right index
  # if nothing is found return -1
  
  while l<= r:
    mid = (l+r)//2
    if x == arr[mid]:
      return mid
    elif arr[mid] > x:
      r = mid -1
    else:
      l = mid+1
  
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


#Time Complexity = O(log(n))