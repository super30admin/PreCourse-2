#Time Complexity: nlogn
#Space Complexity: nlogn
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    i = low
    j = high - 1
    pivot = arr[high]
    while i < j:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i

#write your code here

def quickSortIterative(arr, l, h):
    size=h-l+1
    stack=[0]*size
    top=-1

    top+=1
    stack[top]=l
    top+=1
    stack[top]=h

    while top>=0:
        h=stack[top]
        top-=1
        l=stack[top]
        top-=1

        pos=partition(arr,l,h)

        if l<pos-1:
            top+=1
            stack[top]=l
            top-=1
            stack[top]=p-1
            top-=1


        if h>pos+1:
            top += 1
            stack[top]=pos+1
            top+=1
            stack[top]=h

  #write your code here

  # Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
  print("%d" % arr[i])


