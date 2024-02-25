# Python program for implementation of Quicksort
# Time Complexity : worst-O(n^2) average-O(nlogn)
# Space Complexity : O(logn)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : No
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    i = l - 1
    pivot = arr[h]

    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]

    return i+1


def quickSortIterative(arr, l, h):
  #write your code here
    #using a list to stimulate a stack with intial and high indices
    stack = [(l,h)]

    while stack:
        l, h = stack.pop()
        if l<h:
            p = partition(arr,l,h)

            #push indices of left subarray
            stack.append((l,p-1))
            #push indices of right subarray
            stack.append((p+1,h))

arr = [6,3,5,2,8,1]
n=len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i], end=" ") 

