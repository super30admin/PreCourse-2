# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
      #selecting highest element as pivot
    pivot= arr[high]
    # print('printing the pivot element',pivot)
    #initial index
    i= low-1

    for j in range(low,high):
        if(arr[j]<pivot):
            # initial index of i
            i+=1
            arr[i], arr[j]=arr[j], arr[i]

    arr[i+1], arr[high]=arr[high], arr[i+1]
    return i+1


def quickSortIterative(arr, low, high):
  #write your code here
  #implementation using stack
  stack=[]
  stack.append((low,high))
  while stack:
      low,high=stack.pop()
      if(low<high):
        partition_index= partition(arr, low, high)
        stack.append((low,partition_index-1))
        stack.append((partition_index+1,high))
      


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 