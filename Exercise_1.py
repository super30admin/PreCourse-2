# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, left, right, x): 
    #write your code here
    if((left+right)%2 == 0):

        mid = int((left+right)/2)

    else:

        mid = int(((left+right) - 1)/2)

    if(arr[mid] == x):
        print('Martch: ',mid)
        return mid

    if(x < arr[mid]):

        binarySearch(arr, left, mid, x)

    elif(x > arr[mid]):

        binarySearch(arr, mid, right, x)

    return None
    
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index: ",format(result))
else: 
    print("Element is not present in array")
