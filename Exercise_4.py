# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) <= 1:
    return arr

  # find the mid index
  mid  = len(arr) // 2
  # recursively sort the left and right halves
  left_half = mergeSort(arr[mid:])
  right_half = mergeSort(arr[:mid])
  
  # call merge function to merge the sorted halves
  return merge(left_half, right_half)
  
def merge(left_half, right_half):
  i = j = 0
  merged = []
  
  while i < len(left_half) and j < len(right_half):
    if left_half[i] <= right_half[j]:
        merged.append(left_half[i])
        i += 1
    else:
        merged.append(right_half[j])
        j += 1
        
  # if there are remaining elements in left_half, add them
  merged.extend(left_half[i:])
  merged.extend(right_half[j:])
  
  return merged
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)): 
        print(arr[i], end = " ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
