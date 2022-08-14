# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
    pivot = arr[high]
    i = low-1
    
    for j in range(low,high):
        if arr[j]<= pivot:
            i = i+1
            arr[i], arr[j] =arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return i+1



def quickSortIterative(arr, l, h):
  #write your code here
  s = h -l +1
  stack = [0] * s
  top = -1
  top +=1
  stack[top] = l
  top +=1
  stack[top] = h
  
  
  while top >=0:
      h = stack[top]
      top -=1
      l = stack[top]
      top -=1
      
      pivot = partition(arr,l,h)
      
      if pivot -1 >l:
          top +=1
          stack[top]=l
          top+=1
          stack[top]= pivot-1
      if pivot+1<h:
          top +=1
          stack[top]=pivot+1
          top+=1
          stack[top]= h




  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
