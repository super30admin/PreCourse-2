# Python program for implementation of MergeSort 
from heapq import merge
#using divide and conquer approach
#divide the array into sub arrays until only single element is left in each subarray
#merge the subarrays (sort them while merging) to finally get the original array
def merge(left,right):
  
  arr1=[]  
  i,j=0,0
  #comparing left and right subarrays,by traversing through them element by element
  while i<len(left) and j<len(right):
    #if element in left subarray less than element in right subarray

    if left[i]<=right[j]:
      arr1.append(right[j])
      j=j+1
    else:
      arr1.append(left[i])
      i=i+1
  #add the remaining elements to the newlist
  return arr1+left[i:]+right[j:]

def mergeSort(arr):
  #base case
  if len(arr)>1:
    #find the midpoint 
    middle=len(arr)//2
    #divide the aray into two parts
    left=arr[:middle]
    right=arr[middle:]
    
    
    return merge(mergeSort(left),mergeSort(right))
  else:
    return arr





  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    #arr2=[1,9,8,5,6]
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(mergeSort(arr)) 
