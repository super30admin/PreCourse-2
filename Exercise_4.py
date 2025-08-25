# Time Complexity : O(N * (Log(Base 2) N)) -- O(Log(Base 2) N) is for the steps taken to dividing the array into 2 parts on each step.
# O(N) is for the merging step
# Space Complexity : O(N) -- creating a temp array when merging the left and right parts
# Did this code successfully run on Leetcode : Could not find it on Leetcode
# Any problem you faced while coding this : I went through Algorithm explanation and psuedo code and then was able to implement it


# Your code here along with comments explaining your approach
# Here I have written the code for Sorting in Ascending Order. I believe with minor tweak in the merge routine we can Sort the array in
# Descending Order as well. Keep dividing the array into half length each until we reach 1 element. Then when we merge, we compare
# the elements of two divided arrays and place the elements in a sorted way in the new array and then merge it with the actual array

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  def mergeSortRecur(arr, low, high):
    # base case to stop the recursion
    if(low >= high):
      return
     
    mid = (high + low) // 2
    # divide into left part
    mergeSortRecur(arr, low, mid)
    # divide into right part
    mergeSortRecur(arr, mid + 1, high)

    # merge routine
    p1 = low
    p2 = mid + 1
    temp = []
    while((p1 <= mid) and (p2 <= high)):
      if(arr[p1] <= arr[p2]):
        temp.append(arr[p1])
        p1 += 1
      else:
        temp.append(arr[p2])
        p2 += 1

    while(p1 <= mid):
      temp.append(arr[p1])
      p1 += 1

    while(p2 <= high):
      temp.append(arr[p2])
      p2 += 1

    # update the actual array
    k = low
    for i in range(len(temp)):
      arr[k] = temp[i]
      k += 1
     
  if((len(arr) == 0) or (len(arr) == 1)):
    return
  mergeSortRecur(arr, 0, len(arr) - 1)
  
# Code to print the list 
def printList(arr):
    
  #write your code here
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)
    print("-----------------")
    arr = [12]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)
    print("-----------------")
    arr = []  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)
