# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
    p=arr[high]
    temp=low
    def swap(arr, a, b):
        t=arr[a]
        arr[a]=arr[b]
        arr[b]=t
    for i in range(low, high):
        if(arr[i]<=p):
            swap(arr, i, temp)
            temp+=1

    swap(arr,high, temp)
    return temp

def quickSortIterative(arr, l, h):
  # loop=0
  p=partition(arr, l, h)
  while(h-l>1):
      # loop+=1
      if(p-1>l):
          h=p-1
          p=partition(arr, l, h)
  l=0
  h=len(arr)-1
  while(h-l>1):
      if(p+1<h):
          l=p+1
          p=partition(arr, l, h)
  #write your code here
  pass

arr = [10, 7, 8, 9, 1, 1, 2, 3, 4, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 