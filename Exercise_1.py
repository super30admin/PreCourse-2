# -*- coding: utf-8 -*-
"""
# Python code to implement iterative Binary  
# Search. 
Time Complexity : O(logn) where n is the no. of elemnets in the array 

"""

  
# It returns location of x in given array arr  
# if present,else returns -1 

def binarySearch(arr, l, r, x):
    while l <= r:#base condition of array right most index always greater than left most index
        m = int((l + r)/2) #calculate midpoint of array
        if arr[m] == x: #check if element is middle of array
            return m
        elif x > arr[m]: #if element is greater by mid value then ignore left array
             l = m + 1 #Assign left index as mid index + 1
        else:               #if element is lesser than mid value, then ignore right array
             r = m - 1  #change right index to mid index -1
    return -1 #return -1 for unsuccesful search
      
  
# Test array 
arr = [2,10,40,41,45,90,100] 
x = 2
n = len(arr)
  
# Function call 
result = binarySearch(arr, 0, n - 1, x)
  
if result == -1:
    print("Element is not present in array") 
else:
    print("Element is present at index:",result + 1) #index starts at 0, hence index+1 
    
    
    
""" Recursive Binary Search """
    
    '''  
def binarySearch(arr, l, r, x):
  if r >= l:#base condition of array right most index always greater than left most index
        m = int((l + r)/2) #calculate midpoint of array
        if arr[m] == x: #check if element is middle of array
            return m
        elif arr[m] > x: #check if element is situated in the first half of array
            return binarySearch(arr, l, m-1, x) #search in the first half of array
        elif x > arr[m]: #check if element is present in second half of array
            return binarySearch(arr, m + 1, r, x)#serach in second half of array
    else:
            return -1 #if elem not found
'''



        