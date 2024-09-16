# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here

  pivotindex=h

  pindex=l


  for i in range(l,h+1,1):
      if arr[i]<arr[pivotindex]:
          arr[i],arr[pindex]=arr[pindex],arr[i]
          pindex+=1

  arr[pindex],arr[pivotindex]=arr[pivotindex],arr[pindex]


  return pindex

def quickSortIterative(arr, l, h):
  #write your code here

  stack=[0]*len(arr)

  stack.append(l)

  stack.append(h)

  while len(stack)>1:

      h=stack.pop()
      l=stack.pop()

      partitionindex=partition(arr,l,h)

      if partitionindex-1>l:
          stack.append(l)
          stack.append(partitionindex-1)


      if partitionindex+1<h:
          stack.append(partitionindex+1)
          stack.append(h)



arr=[6,5]

print('Before',arr)

quickSortIterative(arr,0,len(arr)-1)

print('After',arr)
