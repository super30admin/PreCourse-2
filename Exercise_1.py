#O(log n) worst case, O(1) for best case

def binarySearch(arr, l ,r, x):
  while(l<=r):
    mid_point = (l+r)//2
    if arr[mid_point] == x:
      return mid_point
    
    elif x>arr[mid_point]:
      l = mid_point+1
    elif x<arr[mid_point]:
      r = mid_point-1
  return -1


def recursive_binarySearch(arr, l, r, x): 
  mid_point = (l+r)//2
  print(l, mid_point,r)
  if arr[mid_point] == x:
    return  mid_point
  
  elif x>arr[mid_point]:
    return binarySearch(arr,mid_point+1,len(arr)-1, x)
  
  elif x<arr[mid_point]:
    return binarySearch(arr,0,mid_point, x)

    
  
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
