# Python program for implementation of MergeSort 
"""
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
def merge(left, right):
  merged = []
  i = 0
  j = 0
  
  # compare elements from both halves and merge them sorted
  while i<len(left) and j<len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
      
  # add remaining elements (one of these will be non-empty)
  merged.extend(left[i:])
  merged.extend(right[j:])
  
  return merged

def mergeSort(arr):
  #write your code here
  if len(arr) <= 1:
    return arr  # base case: already sorted
  
  mid = len(arr)//2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])
  return merge(left, right)
  
# Code to print the list 
def printList(arr): 
  #write your code here
  print(", ".join(map(str, arr)))
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is")  
    printList(arr)  
    print("Sorted array is: ", end="\n") 
    printList(mergeSort(arr)) 