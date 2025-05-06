# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity - Best case: O(1) - Element found at the middle in the first comparison
                    # Worst and Average case: O(log n) - array divided in half at each step

#  Space Complexity - O(1) — no call stack


def binarySearch(arr, l, r, x): 
      #write your code here

    while (l <= r):
      mid = (l + r) // 2  # Find the middle index

      if arr[mid] == x: # If the element is found at mid, return 
          return mid
      
      elif arr[mid] < x:  # If the element is greater than mid, ignore left half
          l = mid + 1
      
      else:
          r = mid - 1 #  # If the element is lesser than mid, ignore right half

    # Not found
    return -1


if __name__=="__main__":
    
    # Test array 
    arr = [ 2, 3, 4, 10, 40 ] 
    x = 10
      
    # Function call 
    result = binarySearch(arr, 0, len(arr)-1, x) 
      
    if result != -1: 
        print ("Element is present at index % d" % result )
    else: 
        print ("Element is not present in array")
