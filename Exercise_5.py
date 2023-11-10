"""
Time Complexity : O(nlogn)
Space Complexity : O(1)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : yes


Your code here along with comments explaining your approach

""" 

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here

  low = l-1
  pi = arr[h]

  for j in range(l,h):
    if arr[j] < pi:
      low += 1
      arr[j], arr[low] = arr[low], arr[j]

  arr[low +1], arr[h] = arr[h], arr[low+1]

  return low +1

def quickSortIterative(arr, l, h):
  #write your code here

  #create a temp stack
  _size =( h - l +1 )
  stack = [0] * _size

  top = -1

  top  = top + 1
  stack[top] = l
  top = top + 1
  stack[top] = h

  #keep poping from stack while it is not empty
  while top >=0:
    h = stack[top]
    top = top -1
    l = stack[top]
    top = top -1

    #sorted array
    pi = partition(arr, l, h)

    #push left side to stack
    if pi-1 > l:
      top  = top + 1
      stack[top] = l
      top = top +1
      stack[top] = pi -1

    #push right side to stack

    if pi +1 < h:
      top = top + 1
      stack[top] = pi + 1
      top = top +1
      stack[top] = h

# Code to print the list 
def printList(arr): 
  if len(arr) == 0:
    return 

  for i in range(len(arr)):
    print(arr[i], end = " ")
  print()  


# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    quickSortIterative(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

