# Python program for implementation of Quicksort
# Time complexity : o(nlogn)
# space complexity o(n)

# This function is same in both iterative and recursive
def partition(arr, low, high):
    left, pivot = low, arr[high]
    for i in range(low, high):
        if arr[i] < pivot:
            temp = arr[i]
            arr[i] = arr[left]
            arr[left] = temp
            left+=1
    arr[high] = arr[left]
    arr[left] = pivot
    return left


def quickSortIterative(arr, l, h):
   size = h-l+1
   stack = [0]*size
   top=-1
   top =top+1
   stack[top]= l
   top+=1
   stack[top]=h
   while top>=0:
    h = stack[top]
    top-=1
    l = stack[top]
    top-=1
    pivot = partition(arr, l, h)
    if pivot-1>l:
      top = top+1
      stack[top] = l
      top+=1
      stack[top] = pivot-1
    if pivot+1<h:
      top+=1
      stack[top]=pivot+1
      top+=1
      stack[top]= h
    


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5,11]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("% d" % arr[i]),

