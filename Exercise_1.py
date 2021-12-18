#Time Complexity : 0(N)
def binarySearch(arr,l,r,x):
    while l <= r:
        middle = (l+r)//2
        if arr[middle] < x: 
            l = middle+1
        elif arr[middle] > x: 
            r = middle - 1
        else:
            return middle
    return -1
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
result = binarySearch(arr,0,len(arr)-1,x)
if result!=-1:
    print(f'Element is present at index {result}')
else:
    print(f'Element not in array')
