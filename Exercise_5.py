# Python program for implementation of Quicksort


def swap(a,b):
    temp = arr[a] 
    arr[a]=arr[b]
    arr[b]=temp

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    pi = l
    pivot = arr[h]

    for i in range(l,h):
        if(arr[i]<= pivot):
            swap(i,pi)
            pi += 1
    swap(pi,h)
    return pi

def quickSortIterative(arr, l, h):
  #write your code here
  iStack=[]
  iStack.append(l)
  iStack.append(h)

  while(len(iStack)>0):

    #popping l and h

    h = iStack.pop()
    l = iStack.pop()

    index = partition(arr,l,h)

    if index-1 > l:
      iStack.append(l)
      iStack.append(index-1)
    
    if index+1 < h:
      iStack.append(index+1)
      iStack.append(h)

#Driver code
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1)
print("Sorted array using iterative:") 
for i in range(n): 
    print(arr[i]) 