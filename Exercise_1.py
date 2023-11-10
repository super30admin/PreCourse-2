
#time complexity: O(log n) search space is reduced by half each time.
#space complexity: O(1)

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  while(l<=r):
    mid = (l+r)//2   # mid is the middle element of left and right pointers
    if(arr[mid]==x): #return mid if element at mid is equal to the target
      return mid
    elif(arr[mid]>x): #if element at mid is greater than target, right pointer should be before mid(reducing search space)
      r=mid-1
    else:    # if element at mid is smaller than target, left pointer will move after mid
      l=mid+1
  return -1   #condition r>l, comes out of loop  which means target not found hence return false
  

  
# Test array 
arr = [2, 3, 4, 10, 40] #array is sorted, thus can use binary search directly
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
