# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    # pick the last element as pivot
      piv = arr[h]
      i = l-1

      #compare all element with pivot
      for j in range(l,h):
          if arr[j] <= piv:
              i = i+1
              (arr[i],arr[j]) = (arr[j],arr[i])
      (arr[i+1], arr[h]) = (arr[h], arr[i+1])
      return i+1

def quickSortIterative(arr, l, h):
  #write your code here
    size = h-l +1
    stc = [0] * (size)

    top = -1
    top += 1
    stc[top] = l
    top += 1
    stc[top] = h

    while top >=0:
        h = stc[top]
        top -= 1
        l = stc[top]
        top -= 1

        p = partition(arr, l, h)

        if p-1 > l:
            top = top + 1
            stc[top] = l
            top = top + 1
            stc[top] = p - 1

        if p+1 < h:
            top = top + 1
            stc[top] = p + 1
            top = top + 1
            stc[top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

