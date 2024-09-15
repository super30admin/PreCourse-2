# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
    start_index = l
    end_index = r
    mid_index = 0

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_num = arr[mid_index]
        if mid_num == x:
            return mid_index

        if x > mid_index:
          start_index = mid_index + 1
        else:
          end_index = mid_index - 1

    return - 1 
 
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index {result}") 
else: 
    print("Element is not present in array")
