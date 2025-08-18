# Python program for implementation of MergeSort 

"""
TC: O(NlogN) (since we dividing for logN times and merging each of this time for N elements)
SC: O(N) (we are using extra space while merging two lists together)
"""

def mergeSort(arr):
  #write your code here
  if len(arr) <= 1: #base case when further divison is not possible
      return arr

  mid = len(arr)//2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])

  merged = merge(left, right)

  for i in range(len(merged)):
    arr[i] = merged[i]
  
  return arr

def merge(left, right):

  ans = []
  i = 0
  j = 0

  while i<len(left) and j<len(right):
    if left[i] < right[j]:
        ans.append(left[i])
        i+=1
    else:
        ans.append(right[j])
        j+=1
  ans.extend(left[i:])
  ans.extend(right[j:])
  
  return ans
    
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for each in arr:
      print(each)
    print()

    # print("".join(map(str, arr)))
    

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
