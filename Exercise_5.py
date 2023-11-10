# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
from tkinter import E

#Time complexity - 
#Space complexity - 

#the same partition function used in recursive quick sort 
def partition(arr, l, h):
  #write your code here
  i=l-1
  

  pivot=arr[h]
  for j in range(l,h):

    if arr[j]<=pivot:
      i=i+1
      arr[i],arr[j]=arr[j],arr[i]
    
  arr[i+1],arr[h]=arr[h],arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here

  #create a stack
  size=(h-l)+1
  explict_stack=[0]*size
  
  element=-1
  #initialize initial indexes into stack

  element=element+1
  explict_stack[element]=l
  element=element+1
  explict_stack[element]=h

  #loop until zero elements left in stack
  while len(explict_stack)>0:

    #pop h and l
    h=explict_stack[element]
    element=element-1
    l=explict_stack[element]
    element=element-1

    #find partition index
    p=partition(arr,l,h)

    #if left side of pivot has elements push those indices to stack
    if p-1>1:
      element=element+1
      explict_stack[element]=l
      element=element+1
      explict_stack[element]=p-1
    #if there are elements to the right of pivot , push those indices to stack

    if p+1<h:
      element=element+1
      explict_stack[element]=p+1
      element=element+1
      explict_stack[element]=h

  

def printList(arr): 
    print(arr)
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    #arr2=[1,9,8,5,6]
    print ("Given array is", end="\n")  
    printList(arr) 
    quickSortIterative(arr,0,len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 




