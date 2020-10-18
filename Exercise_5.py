# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i=-1
  pivot=arr[h]
  for j in range(l,h):
      if arr[j]<=pivot:
          i=i+1
          arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[h]=arr[h],arr[i+1]
  print(arr)
  return i+1


def quickSort(arr, l, h):
   if l<h: ##why do we have to do this?
        pi=partition(arr,l,h)
        quickSort(arr,l,pi-1)
        quickSort(arr,pi+1,h)


arr = [10,20,30,50,40]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),

