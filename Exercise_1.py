# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 


"""
Algorithm : 
start = l end = r
1 . Find the mid element
2 . if mid element in array == x return x
3. if arr[mid] < x : set start = mid + 1
4. else end = mid - 1
5. retiterate 1 -4 until start <= end
"""
def binarySearch(arr, l, r, x): 
  
  #write your code here
  start = l
  end = r
  while start <= end:
  
        mid = int((end - start)*0.5) + start
        if arr[mid] == x:
            return mid
        elif arr[mid] < x :
            start = mid + 1
        else:
            end = mid - 1

  return -1
            
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result )
else: 
    print("Element is not present in array")


