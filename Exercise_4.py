# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) <= 1:
    return arr

  # Split the array into halves
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  # Recursively sort each half
  left_half = mergeSort(left_half)
  right_half = mergeSort(right_half)

  # Merge the sorted halves
  return merge(left_half, right_half)



def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Merge elements in sorted order
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Append the remaining elements (if any)
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result
  
  
  
# Code to print the list 
def printList(arr): 
    
  for elements in arr:
    print(elements)
      
  
# driver code to test the above code 
if __name__ == '__main__': 
  arr = [12, 11, 13, 5, 6, 7]  
  print ("Given array is", end="\n")  
  printList(arr) 
  sorted_array = mergeSort(arr) 
  print("Sorted array is: ", end="\n") 
  printList(sorted_array) 
