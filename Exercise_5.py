#Time Complexity is nlogn for the average and best case and for worst case is n^2
#Space complexity is logn as the two stack is used with half length of the array 
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  #here pivot variable will be the base to make partition of the array
  pivot = arr[l]
  i = l+1
  j = h
  while(i<j):
    #while loop will work till the value greater then the pivot element will be encounter
    while (arr[i]<=pivot and i < h):
      i = i + 1
    #while loop will work till the value lower then the pivot element will encounter
    while(arr[j]>pivot and j>l):
      j = j-1
    #value greater then pivot from left to right and value less then pivot right to left will swap
    if(i<j):
      arr[i], arr[j] = arr[j], arr[i]
  #partition will occur according to the pivot element
  arr[l], arr[j] = arr[j], arr[l]
  #position of the partition will be returned
  return j

def quickSortIterative(arr, l, h):
  #write your code here
  #intialising the size of the stack
  StackSize = (h-l+1)//2
  #defining the stack size for putting the the lower value for sub array 
  LowerStack = [0]*StackSize
  #defining the stack size for putting the the upper value for sub array 
  UpperStack = [0]*StackSize

  top = 0
  LowerStack[0]=0
  UpperStack[0]= len(arr)-1
  #while loop will work till there are elements in the lowerstack and upperstack
  while top>-1:
    start = LowerStack[top]
    end = UpperStack[top]
    #decrementing stack pointer 
    top-=1
    #storing the value for the partition
    j_location = partition(arr, start, end)

    #sort at the left subarray 
    if start< j_location:
      top+=1
      LowerStack[top] = start
      UpperStack[top] = j_location -1

    #sort at the right subarray
    if j_location+1<end:
     top+=1
     LowerStack[top] = j_location+1 
     UpperStack[top] = end

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),
