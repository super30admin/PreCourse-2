# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    if x in arr:
        for location,each in enumerate(arr):
            if each == x:
                return location
    return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
# result = binarySearch(arr, 0, len(arr)-1, x)
#
# if result != -1:
#     print("Element is present at index % d" % result)
# else:
#     print ("Element is not present in array")

tg = [(1,2),(3,4),(4,5)]

for i in range(len(tg)):
    key = tg[i][0]
    val = tg[i][1]
    if i == 1:
        tg.pop(0)
        break

print(tg)
