# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) == 1:
    return arr

  
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]
  mergeSort(left)
  mergeSort(right)
  
  left_index = right_index = sorted_index = 0
  
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      arr[sorted_index] = left[left_index]
      left_index += 1
    else:
      arr[sorted_index] = right[right_index]
      right_index += 1
    
    sorted_index += 1
  
  while left_index < len(left):
    arr[sorted_index] = left[left_index]
    left_index += 1
    sorted_index += 1
  
  while right_index < len(right):
    arr[sorted_index] = right[right_index]
    right_index += 1
    sorted_index += 1
    
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for element in arr:
      print(element, end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
