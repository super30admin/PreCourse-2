# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    index = l - 1  # low - Starting Index , partition Index
    pivot = arr[h] # last element as pivot , high - End Index
  
    for i in range(l,h):

        if arr[i] <= pivot: # check if current element is smaller than or equal to pivot
            index = index + 1
            arr[index], arr[i] = arr[i], arr[index]
    #swap the last element, return partition index
    arr[index+1], arr[h] = arr[h], arr[index+1] 
    return (index+1) 


def quickSortIterative(arr, l, h):
    #use stack to replace recursion to iterative
    stack = []
    stack.append(l)
    stack.append(h)

    while(stack):
      #pop high first, then low -Stack LIFO
      high = stack.pop()
      low = stack.pop()

      partitionIndex = partition(arr,low,high)

      if partitionIndex-1 > low:
        stack.append(low)
        stack.append(partitionIndex - 1)

      if partitionIndex + 1 < high:
        stack.append(partitionIndex+1)
        stack.append(high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 




