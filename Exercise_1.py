"""
Time Complexity : O( log(n) )
Space Complexity : O(n)
"""
def BinarySearch(array, element):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array = [3,6,7,9,10]
result = BinarySearch(array, 10)
print(result)
