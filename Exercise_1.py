#Time Complexity :
# O(Log N)

#Space Complexity :
# O(N)

#Did this code successfully run on Leetcode :
#Yes

#Any problem you faced while coding this :
#No

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
    #write your code here
    target = x

    #If there is only 1 element in the array, then check if that is the target
    if len(arr[l:r+1]) ==  1 :
        if arr[l] == target:
            return l+1
        else :
            return -1

    #If there are only 2 elements in the array, then check if any of them is the target
    elif len(arr[l:r+1]) ==  2 :
        if arr[l] == target:
            return l +1 
        elif arr[r] == target :
            return r + 1
        else :
            return -1

    #Check if the centre element is the target 
    elif arr[int((l+r+1)/2)] == target :
        return int((l+r+1)/2) + 1

    #Check if the target is greater than centre element, then call search on the second half of the array 
    elif arr[int((l+r+1)/2)] < target :
        return binarySearch(arr, int((l+r+1)/2),r,target)

    #Check if the target is smaller than centre element, then call search on the first half of the array i
    elif arr[int((l+r+1)/2)] > target :
        return binarySearch(arr,l, int((l+r+1)/2),target)
  
# Test array 
arr = [ 2, 3, 4, 10, 40] 
x = 4
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
if result != -1: 
    print (f'Element is present at index {result}' )
else: 
    print ("Element is not present in array")
