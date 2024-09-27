# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[l]
  j = h
  for i in (range(l+1,h+1)) :
    if arr[i]>= pivot and i<j :

      arr[i],arr[j] = arr[j], arr[i]
      j = j-1

      print(arr)

      
    
  arr[l],arr[j] = arr[j],arr[l]
  print(arr[l],arr[j], "pivot swap")
  print(arr)
  print(j, "pivot position")
  return j


      
  

  #write your code here


def quickSortIterative(arr, l, h):
  if l < h:

    pivot = partition(arr,l,h)
    print(pivot)
    quickSortIterative(arr, l, pivot-1)
    quickSortIterative(arr,pivot,h)
  #write your code here


if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", arr)  
    quickSortIterative(arr,0,5) 
    print("Sorted array is: ", arr) 
     


