# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here

    p=arr[high]
    i=low
    for j in range(low, high+1):
        if arr[j]<p:
            arr[i], arr[j]=arr[j], arr[i]
            i+=1
    arr[i], arr[high]=arr[high], arr[i]
    #write your code here
    return i
      


def quickSortIterative(arr, low, high):
  #write your code here

  new_s=high-low+1
  stack=[0 for i in range(new_s+1)]

  top=0
  
  stack[top]=low
  top+=1
  stack[top]=high


  while top>=0:

    h=stack[top]
    top-=1
    l=stack[top]
    top-=1

    p=partition(arr,l,h)

    if p-1>l:
      top+=1
      stack[top]=l
      top+=1
      stack[top]=p-1
    if p+1 <h:
      top=top+1
      stack[top]=p+1
      top=top+1
      stack[top]=h


arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 