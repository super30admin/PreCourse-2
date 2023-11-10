# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

# Time Complexity : Best Case and Average Case - O(n log n), Worst Case -O(n^2)
# Space Complexity :Best Case and Average Case - O(log n), Worst Case- O(n)

def partition(arr, l, h):
  pivot=arr[h]
  i=l-1
  
  for j in range (l,h):
    if arr[j]<pivot:
      i+=1
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp

  temp=arr[i+1]
  arr[i+1]=arr[h]
  arr[h]=temp
  
  return i+1 

def quickSortIterative(arr, l, h):
  #write your code here
  stack=[]
  stack.append((l,h))

  while stack:
    l,h=stack.pop()

    p=partition(arr,l,h)
    
    if p-1>l:
      stack.append((l,p-1))
    
    if p+1<h:
      stack.append((p+1,h))

    print(arr)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 