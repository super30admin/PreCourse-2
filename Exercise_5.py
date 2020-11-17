#  Time Complexity : O(NlogN)
#  Space Complexity : O(N)
#  Did this code successfully run on Leetcode : yes
#  Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = l - 1 
    pivot = arr[h]  # 10, 7, 8, 9, 1, 5 
    for j in range(l,h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    i = i + 1 # mid point : having all left elements smaller and having all right elements larger  
    arr[i], arr[h] = arr[h],arr[i]
    return i


def quickSortIterative(arr, l, h):
      stack = []
      stack.append(l)
      stack.append(h)

      while stack:
            h = stack.pop()
            l = stack.pop()
            p = partition(arr,l,h)
            if p-1 > l :
                  stack.append(l)
                  stack.append(p-1)
            if p+1 <h:
                  stack.append(p+1)
                  stack.append(h)


# arr = [4, 3, 5, 2, 1, 3, 2, 3] 
# n = len(arr) 
# quickSortIterative(arr, 0, n-1) 
# print ("Sorted array is:") 
# for i in range(n): 
#     print ("%d" %arr[i]), 

'''
approch : recursive 
'''


