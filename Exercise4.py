# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No


# Python program for implementation of MergeSort 

def merge(arr, low, mid, high):
  temp = []
  left = low
  right = mid + 1
  while left <= mid and right <= high:
    if arr[left] <= arr[right]:
      temp.append(arr[left])
      left = left + 1
    else:
      temp.append(arr[right])
      right = right + 1
  while left <= mid:
    temp.append(arr[left])
    left = left + 1
  while right <= high:
    temp.append(arr[right])
    right = right + 1
  for i in range(low, high+1):
    arr[i] = temp[i-low]



def ms(arr, low, high):
  if low < high:
    mid = (low+high)//2
    ms(arr, low, mid)
    ms(arr, mid+1, high)
    merge(arr, low, mid, high)

def mergeSort(arr):

  #write your code here
  ms(arr, 0, len(arr)-1)

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