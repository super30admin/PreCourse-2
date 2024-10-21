# // Time Complexity : O(nlog(n)) for division and O(n^2) worst case for extreme pivots.
# // Space Complexity : O(log(n)) space logarithmc due to stack
# // Did this code successfully run on Leetcode :NA
# // Any problem you faced while coding this : No.

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    i = l
    j = h - 1
    pivot = arr[h]

    while i < j:
        while i < h and arr[i] <pivot:       # i moves from left to right
            i +=1

        while j > l and arr[j] >= pivot:     # j moves from right to left
            j -= 1

        if i < j:                            # after j crosses i 
            arr[i],arr[j] = arr[j],arr[i]    # swap

    if arr[i] > pivot:                       # after i crosses pivot
        arr[i],arr[h] = arr[h],arr[i]        # swap pivot location
    
    return i                                 # return pivot index     

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((0, len(arr) - 1))

  while stack:
      l,h = stack.pop()                      # unpack tuple size for every array ex-(0,4)

      if h <= l:                             # check if subarray has only one/zero elements
          continue                           # done

      p = partition(arr, l, h)
      stack.append((l, p - 1))              # left subarray
      stack.append((p + 1, h))              # right subarray


arr = [10, 7, 8, 9, 1, 5, 11, 21312, 122, 214, 2, 333] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end = " ")
  