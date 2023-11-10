# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 

    while (l <= r):
        med = l + (r - l) // 2

        if (arr[med] > x):
          r = med - 1

        elif(arr[med] < x):
            l = med +1

        else:
          return 'Element found and the position of x is %d', med


    return -1



arr = [3, 5, 6,  7, 9, 10, 12, 14, 19, 23, 27, 29]
x = 10
res = binarySearch(arr, 0, len(arr) - 1, x)
print(res)