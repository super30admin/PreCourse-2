def merge(left_arr, right_arr):
  merged = []
  i = 0
  j = 0

  while i < len(left_arr) and j < len(right_arr):
    if left_arr[i] < right_arr[j]:
      merged.append(left_arr[i])
      i += 1
    else:
      merged.append(right_arr[j])
      j += 1

  while i < len(left_arr):
    merged.append(left_arr[i])
    i += 1

  while j < len(right_arr):
    merged.append(right_arr[j])
    j += 1

  return merged

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  
  #write your code here
  l = 0
  r = len(arr)-1
  mid = (l+r)//2
  left_arr = mergeSort(arr[:mid])
  right_arr = mergeSort(arr[mid:])

  return merge(left_arr, right_arr)

# Code to print the list 
def printList(arr): 

    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
