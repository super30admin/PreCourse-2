"""
Exercise_1 : Python code to implement iterative Binary Search
Time Complexity :
    Best Case- O(1)
    Worst Case- O(logn).
Space Complexity : O(1) 
    As we need two variable to keep track of the range of elements that are to be checked and No other data is needed.


Binary Search works in the following way:
    there are 2 pointer Left and Right which is used to calculate the mid index [left + right]/2
    The Aim is to find the Key equal to the the value present in the mid index or else the Key is not present
    
    there are 2 condition if the arr[mid] is not the key:
        key < mid the Right becomes mid-1 OR
        key > mid then Left becomes mid +1
        
    This process continue until Left <= Right

@name: Rahul Govindkumar_RN27JUL2022
"""
# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    
  #write your code here    
  
  #Loop until Left pointer < = Right pointer
    while (l <= r):
        
  #Calculate mid index        
        mid = (l+r)//2
        
  #If Key is Found 
        if (arr[mid]==x):
            return mid
        
        if (x < arr[mid]):
            r = mid -1
            
        else:
            l = mid+1    
            
    return -1
   
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 188
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element %d is present at index %d" %(x ,result) )
else: 
    print ("Element %d is not present in array" %x)
