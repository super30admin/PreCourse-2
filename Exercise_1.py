# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#Time Complexity : Each recursive call divides the array into half. O(log n)
#Space Complexity : o(1) because its an iterative process 
#Approach: we used while loop as a iterative approach to find the value of x
def binarySearch(arr, l, r, x): 
  
  #write your code here
  while l <= r:
        mid = (l + r) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore the left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore the right half
        else:
            r = mid - 1

    # If we reach here, the element was not present
  return -1

if __name__ == "__main__":  
# Test array 
  arr = [ 2, 3, 4, 10, 40 ] 
  x = 10
    
  # Function call 
  result = binarySearch(arr, 0, len(arr)-1, x) 
    
  if result != -1: 
      print (f"Element is present at index % d" % result )
  else: 
      print ("Element is not present in array")
