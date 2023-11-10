# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#-----------------------------------------------------
# Time Complexity : O(Log n)  ---> n is the number of elements in the array
# Space Complexity : O (log n) ---> n is the number of elements in the array
#---------------------------------------------------


def binarySearch(arr, l, r, x): 
  
  # find middle element in the array
  # In python mid will not overflow hence l+r/2
  mid=(l+r)//2
  # print(arr[mid],arr[l],arr[r])
  # if right is greater than and equal untill then we h=can narrow our results
  if r >= l:
    # if middle element is equal to the x (our finding element)
    if arr[mid]==x:
      # print(mid)
      # return the index of the middle element
      return mid
    #if the x greater then it will be in the end of the array so we change our mid  
    elif (x>arr[mid]):
      return binarySearch(arr,mid+1,r,x)
    else:
      # else we change our right to mid-1 if the element is smaller than middle element
      return binarySearch(arr,l,mid-1,x)
  else:
    # if not found 
    return -1
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print ("Element is present at index ",result)
else: 
    print ("Element is not present in array")
