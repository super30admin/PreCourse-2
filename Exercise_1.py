# Binary Search Time Complexity: Best Case: O(1), Worst Case: O(log n)
# Binary Search Space Complexity: O(1)
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  #write your code here
  #Assuming that the list is already sorted
  while l<=r:
    mid=(l+r)//2 #finding the midpoint
    if x==arr[mid]: #if key element is mid return the position
      return mid
    elif x<arr[mid]: #if key element is less than the mid element we search on the left 
        r=mid-1
    else: #if the key element is greater than the mid element we search on the right side of the array
        l=mid+1
  return -1 #if the element is not found we return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", result) 
else: 
    print("Element is not present in array")
