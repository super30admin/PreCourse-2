# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1 
def binary_search(arr, l, r, x):
    if r >= l:
        mid = 1 + int((r - l) / 2)
        print(mid)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call 
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")
