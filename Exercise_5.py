#Time complexity:O(log(n))
#space complexity: O(1)
#Ran in leetcode: yes
#problems/issues: None
# The same as recursive quick sort. But instead of using recursion to find the solution of the left and right half of a pivot, we 
# iteratively find this out using a queue.
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
  pivot=arr[low]
  i=low
  for j in range(low+1,high+1):
      if(arr[j]<pivot):
          temp=arr[i+1]
          arr[i+1]=arr[j]
          arr[j]=temp
          i+=1
  temp=arr[i]
  arr[i]=pivot
  arr[low]=temp
  return i

def quickSortIterative(arr, low, high):
  #write your code here
  if(low>=high):
      return
  Q=[]
  k=partition(arr,low,high)
  Q.append((low,k-1))
  Q.append((k+1,high))
  while(Q):
    low=Q[0][0]
    high=Q[0][1]
    if(low>=high):
      del(Q[0])
      continue
    k=partition(arr,low,high)
    Q.append((low,k-1))
    Q.append((k+1,high))
    del(Q[0])

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),




