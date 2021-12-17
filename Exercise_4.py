# Time Complexity : 
# Best Case: O(N(log(N))) 
# Worst Case: O(N(log(N)))  

# Space Complexity : (Recursion Stack = log(N) + Auxiliarry Array = N)
# Best, Worst, Average Case = O(N)

# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No
def mergeSort(arr):

  def recur(arr):
    if len(arr) == 1:
      return arr

    left = 0
    right = len(arr) - 1
    middle = left + (right - left) // 2

    leftSort = recur(arr[left:middle + 1])
    rightSort = recur(arr[middle + 1:right + 1]) 

    p = 0
    q = 0
    currSorted = []
    while p < len(leftSort) and q < len(rightSort):
      if leftSort[p] <= rightSort[q]:
        currSorted.append(leftSort[p])
        p += 1
      else:
        currSorted.append(rightSort[q])
        q += 1
    while p < len(leftSort):
      currSorted.append(leftSort[p])
      p += 1
    while q < len(rightSort):
      currSorted.append(rightSort[q])
      q += 1
      
    return currSorted
    
  arr[:] = recur(arr)

  #write your code here
  
# Code to print the list 
def printList(arr): 
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
