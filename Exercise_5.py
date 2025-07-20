#Time Complexity :O(n²)
#Space Complexity :O(n)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : none
#Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot=arr[h]               # the last element is choosen as the pivot 
  i=l-1
  for j in range (l,h):
    if pivot>arr[j]:          # check if the element is less than the pivot then it needs to be in the left 
      i=i+1                 
      arr[i],arr[j]=arr[j],arr[i] #swap the elements such that smaller element comes at the beginning
  arr[i+1],arr[h]=arr[h],arr[i+1] # placement of the pivot element correctly
  return i + 1                          # return the index
    


def quickSortIterative(arr, l, h):
    sizeOfStack=h-l+1          # the size of the stack to be defined
    stack=[0]*sizeOfStack      #define the stack and initialise it
    top=-1                     #top of the stack is still not pointing to anything 
    
    top=top+1                  #top of the stack is incremented to hold the value
    stack[top]=l               # the lower end of the array is pushed on the stack
    top=top+1                  #top of the stack is incremented to hold the next value to be pushed 
    stack[top]=h               # the higher end of the array is pushed on the stack

    while top>-1:              # while there are still elements in the stack
        h=stack[top]           # pop the higher end of the array to be sorted 
        top=top-1              # keep the top pointing to the valid place in the stack
        l=stack[top]           # pop the lopwer end of the array to be sorted
        top=top-1              # keep the top pointing to the valid place in the stack

        pivot_index=partition(arr,l,h)   # position of the pivot
        if pivot_index-1>l:              # valid subarray and needs sorting 
            top=top+1                    # keep the top pointing to the valid place in the stack
            stack[top]=l                 # push l on the stack
            top=top+1                    # keep the top pointing to the valid place in the stack
            stack[top]=pivot_index-1     # push the other end of the subarray on the stack
        
        if pivot_index+1<h:               # valid subarray and needs sorting 
            top=top+1                     # keep the top pointing to the valid place in the stack
            stack[top]=pivot_index+1      # push the other end of the subarray on the stack
            top=top+1                     # keep the top pointing to the valid place in the stack
            stack[top]=h                  # push h on the stack
    

def printArray(arr):                      # print the array
    for i in arr:
        print(i)

if __name__ == "__main__":
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    print("Original array:")
    printArray(arr)
    quickSortIterative(arr, 0, len(arr) - 1)
    print("Sorted array:")
    printArray(arr)