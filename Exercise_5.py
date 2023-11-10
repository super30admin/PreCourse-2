# Time Complexity : O(N^2)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class myStack:

     def __init__(self):
         self.stack=[]
         
     def isEmpty(self):
         return self.size() ==0
         
     def push(self, item):
         self.stack.append(item)
         
     def pop(self):
         if self.isEmpty():
             return 'Stack is empty'
         else:
             return self.stack.pop()
        
     def peek(self):
         if self.isEmpty():
             return 'Stack is empty'
         else:
             return self.stack[-1]
         
        
     def size(self):
         return len(self.stack)
         
     def show(self):
         return self.stack

def partition(arr, low, high):
  #write your code here
   #Selecting last element as the pivot element
    pivot=arr[high]
    
    i=low-1
    
    for j in range(low,high):
        #Swapping the elements less than the pivot element to the left and those greater than the pivot elements to the right
        
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[i+1], arr[high]=arr[high], arr[i+1]
    return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  s=myStack()
  s.push(l)
  s.push(h)
  while s.isEmpty() is not True:
      h=s.pop()
      l=s.pop()
      p=partition(arr, l, h)
      if p-1 > l:
          s.push(l)
          s.push(p-1)
      if p+1 < h:
          s.push(p+1)
          s.push(h)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 


