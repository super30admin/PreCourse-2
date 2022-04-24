# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
    '''
    time complexity: O(nlogn)
    space complexity: O(n)
    '''
    #write your code here
    #assign last element as pivot
    
    pivot = arr[high]
    #this index will hold the highest number while itterating
    i = low-1

    for j in range(low,high):
        if(arr[j]<= pivot):
            #if greater element is found shift the pointer
            i+=1

            #swapping element at i with element at j
            #this will keep smaller elemnts on left side and greater element on right side
            (arr[i],arr[j]) = (arr[j],arr[i])

        
    #swapping the pivot, such that all elements smaller then pivot would be on left and other on right
    (arr[i+1],arr[high]) = (arr[high],arr[i+1])

    #return pivot
    return i+1 


def quickSortIterative(arr, l, h):
  '''
  time complexity: O(nlogn)
  space complexity: O(n)
  '''
  #write your code here
  size = h - l + 1
  stack = [0] * size


  top=-1

  top+=1
  stack[top]=l
  top+=1
  stack[top]=h

  while(top>=0):
    h=stack[top]
    top=top-1
    l=stack[top]
    top=top-1

    p = partition(arr,l,h)

    if(p-1>l):
      top+=1
      stack[top]=l
      top+=1
      stack[top]=h

    if(p+1<h):
      top+=1
      stack[top] = p+1
      top=top+1
      stack[top]=h




# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:",arr ) 
