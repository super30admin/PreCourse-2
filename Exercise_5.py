# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    pivot = arr[high]
    pIndex = low
    for i in range(low,high):
        if arr[i]<=pivot:
            swap(arr,i,pIndex)
            pIndex+=1
    swap(arr,pIndex,high)
    return pIndex

def swap(arr,x,y):
   arr[x],arr[y] = arr[y],arr[x]
 

def quickSortIterative(arr, l, h):
    #write your code here
    size = h-l+1
    stack = [0]*size
    t = -1
    
    t+=1
    stack[t] = l
    t+=1
    stack[t] = h


    while t>=0:

      h = stack[t]
      t-=1
      l = stack[t]
      t-=1

      p = partition(arr,l,h)

      if p-1>l:
        t+=1
        stack[t] = l
        t+=1
        stack[t] = p-1

      if p+1<h:
        t+=1
        stack[t] = p+1
        t+=1
        stack[t]=h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 



#TC: O(nlogn)
#TC: O(n)->stack
