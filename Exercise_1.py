# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    #write your code here
    mdpt = int((l + r) / 2)

    if(l > r):
        print(-1)
        -1
    elif arr[mdpt] == x:
        print(mdpt)
        mdpt
    elif x < arr[mdpt]:
        binarySearch(arr, l, mdpt - 1, x)
    else:
        binarySearch(arr, mdpt + 1, r, x)


  
# Test array 
arr = [ 2, 3, 4, 10, 40 ]
x = 10
  
# Function call

result = binarySearch(arr, 0, len(arr)-1, x)
  
if result != -1: 
    #print("Element is present at index % d" % result)
    print(result)
else: 
    print("Element is not present in array")

#edited