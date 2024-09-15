# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):

        if (l>r):
            return -1


        m=int((l+r)/2)
        if (arr[m]==x):

            return m

        elif arr[m]<x:
          return  binarySearch(arr,l+1,r,x)

        else:
           return binarySearch(arr,l,r-1,x)


  
  #write your code here
  
    
  
# Test array
def m():
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)


    if result != -1:
        print (f"Element is present at index {result}")
    else:
        print ("Element is not present in array")
m()