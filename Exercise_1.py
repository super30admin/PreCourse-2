#Time complexity: O(logn)
#Space Complexity: O(1)

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
    if r >= l: #check if the pointers are not crossing at anytime 
      mid = (r+l) // 2 #get the mid value

      if arr[mid] == x: #check if the mid value is the search element
        return mid
      elif arr[mid] < x: # if the mid is less than search element then call the function for mid+1 as left element
        return binarySearch(arr, mid + 1, r, x)
      else: # else call the function for mid-1 as right element
        return binarySearch(arr, l, mid - 1, x)

    else: # if the pointers cross then we dont have the element in the array and return -1
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
