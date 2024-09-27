'''
====== Submission Details =======
Student Name: Pavan Kumar K. N.
Email       : pavan1011@gmail.com
S30 SlackID : RN32MAY2021
=================================
'''

# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time complexity: O(log n) : T(n) = T(n/2) + c
# Space complexity: O(1) 
def binarySearch(arr, l, r, x):
    #arr: input array
    #x  : queried element
    #l  : "leftmost" element
    #r  : "rightmost" element 

    #By definition of left and right, in a valid search array: l<r
    #Step 1: Iterate until search array shrinks to size 1, i.e, l==r
    while l<=r:
        #Step 2: Check if query element (x) is at the midpoint of arr
        #Floor division operator "//" to find midpoint
        mid = (l + r) // 2
        # print(f"mid:{mid}")

        #By law of trichotomy, only 3 possible conditions:
        #Either x == mid or x > mid or x < mid
        
        #Query element at midpoint
        if(arr[mid] == x):
            # print("Found")
            #Step 3(a): Query element found
            return mid
        
        #Step 3(b): Query element is greater than mid point
        elif x > arr[mid]:
            #Drop the search array left of the midpoint
            #By moving "left" to midpoint + 1
            l = mid + 1
            # print(f"l: {l}, r: {r}")

        #Step 3(c): Query element has to be lesser than mid point
        else:
            #Drop the search array right of the midpoint
            #By moving "right" to midpoint - 1
            r = mid - 1
            # print(f"l: {l}, r: {r}")

    #Step 3(d): If conditional loop terminates, element not found
    return -1  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
# The assumption here is that first element is at index 0
# So array of length "n" has max index = n-1
#
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    #Changed print statements to Python3 compliant code.
    print("Element is present at index % d" % result)
else: 
    print("Element is not present in array")
