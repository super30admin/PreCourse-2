# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
# Time Complexity : O(log(n))
# Any problem you faced while coding this : little diffuclt to think in a non-recursive way
def partition(arr, l, h):
  #write your code here
    pivot = arr[h]
    partition = l
    for i in range(l,h):
        if (arr[i] <= pivot):
            temp =  arr[i]
            arr[i] = arr[partition]
            arr[partition] = temp
            partition = partition + 1
    temp = arr[h]
    arr[h] = arr[partition]
    arr[partition] = temp
    return partition


#The difference here would be assigning the low and  high values in left and right lists
#Pop them and keep partitioning and swapping unti  both the lists are empty 
def quickSortIterative(arr, l, h):
  #write your code here
  leftList  = list()
  rightList = list()

  leftList.append(l)
  rightList.append(h)

#  while(len(leftStack)!=0 or len(rightStack)!=0):
  while len(leftList)!=0 and len(rightList)!=0:
    l  = leftList.pop()
    h = rightList.pop()
    pivPos = partition(arr,l,h)
    if (pivPos+1<h):
      leftList.append(pivPos+1)
      rightList.append(h)
    if (pivPos-1>l):
      leftList.append(l)
      rightList.append(pivPos-1)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])

