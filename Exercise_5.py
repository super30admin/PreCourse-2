# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
#Time Complexity: worstcase: O(n**2) averagecase: O(nlogn)
# Space Complexity: O(2n) -> O(n)
def partition(arr,low,high):
  pivot = arr[low]
  i = low + 1
  j = high
  while i <= j:
    while i <= j and arr[i] <= pivot:
      i += 1
    while i <= j and arr[j] >= pivot:
      j -= 1
    if i <= j:
       arr[i],arr[j] = arr[j],arr[i]
  arr[low],arr[j] = arr[j],arr[low]
  return j
  
def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append(l)
  stack.append(h)
  while len(stack) > 0:
    right = stack.pop()
    left = stack.pop()
    if left > len(arr) or left < 0 or right > len(arr) or right < 0:
      break;
    print(left,right)
    part = partition(arr,left,right)
    print(left,part,right)
    if part - 1 > l:
      stack.append(l)
      stack.append(part-1)
    if part + 1 < right:
      stack.append(part+1)
      stack.append(right)





arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 