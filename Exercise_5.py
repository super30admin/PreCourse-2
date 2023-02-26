# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[h] = arr[h], arr[i+1]

    return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []

  stack.append(l)
  stack.append(h)

  while stack : 
    h = stack.pop()
    l = stack.pop()
    p = partition(arr, l, h)

    if l < p-1 : 
      stack.append(l)
      stack.append(p-1) 

    if h > p+1 : 
      stack.append(p+1)
      stack.append(h)




# Driver code to test above 
arr = [4, 3, 5, 2, 1, 3, 2, 3] 
n = len(arr) - 1
quickSortIterative(arr, 0, n) 
print ("Sorted array is:") 
for i in range(n+1): 
    print ("%d" %arr[i])
