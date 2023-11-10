# Python code to implement iterative Binary Search.
# It returns location of x in given array arr if present, else returns -1

# Time complexity: O(log(n))
# Space complexity: O(1)
def binarySearch(arr, l, r, x):
    if len(arr) == 0 or x < arr[l] or x > arr[r]:
        return -1
    while l < r:
        mid = l + (r-l)//2
        # while loop to avoid repetitive elements in the array
        while arr[l] == arr[l+1]:
            l = l+1
        while arr[r] == arr[r-1]:
            r = r-1
        if arr[l] == x:
            return l
        elif arr[r] == x:
            return r
        elif arr[mid] == x:
            return mid
        else:
            # if mid-element is greater than the target, set the end pointer to the next element left of mid-element
            # else start pointer is set next to next element right to the mid-element
            if arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1


# Test array 
arr = [2, 3, 4, 10, 40]
x = 10
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1: 
    print("Element is at the index " + str(result))
else: 
    print("Element is not present in the array")
