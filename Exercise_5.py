# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
#Time Complexity:O(n logn)
def partition(arr, l, h):
  #write your code here
    pivot = arr[h]
    lpos=l-1
    for j in range(l,h):
          if(arr[j]<= pivot):
              lpos=lpos+1
              temp=arr[j]
              arr[j]=arr[lpos]
              arr[lpos]=temp
              
    arr[h]=arr[lpos+1]
    arr[lpos+1]=pivot
    return lpos+1 


def quickSortIterative(arr, l, h):
  #write your code here
  stack=[]
  #FILO
  stack.append(h)
  stack.append(l)
  
  while(len(stack) != 0):
      l=stack.pop()
      h=stack.pop()
     
      pos=partition(arr,l,h)
      #left
      
      if(pos-1>l):
        stack.append(pos-1)
        stack.append(l)
      #right
      if(pos+1<h):
        stack.append(h)
        stack.append(pos+1)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
      

