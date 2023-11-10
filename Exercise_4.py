#Time complexity: O(n logn)
#Space Complexity: O(1)
# Python program for implementation of MergeSort 
# Used the divide concure technique but diving the array in single one and then sorting it to created a whole sorted array
def mergeSort(arr):
  leng = len(arr)
  middle = leng // 2
  left = arr[:middle]
  right = arr[middle:]
  left = mergeSort(left)
  right = mergeSort(right)

  a = 0
  b = 0
  c = 0

while a < len(left) and b < len(right):
  if left[a] < right[b]:
    arr[c] = left[a]
    a += 1
  else:
    arr[c] = right[b]
    b += 1
    c += 1

while a < len(left):
  arr[c] = left[a]
  a += 1
  c += 1

while j < len(R):
    arr[k] = R[j]
    j += 1
    k += 1

  # Implementation
  # len_l = len(left)
  # len_r = len(right)
  # while a <= len_l and b <= len_r:
  #   if left[a] <= right[b]:
  #     blankList.append(left[a])
  #     a += 1
  #   else:
  #     blankList.append(right[b])
  #     b += 1
  # while a < len_l:
  #   blankList.append(left[a])
  # while b < len_r:
  #   blankList.append(right[b])

  # return blankList



  
  #write your code here
  
# Code to print the list 
def printList(arr): 
  i = len(arr)
  while i < len(arr):
    print(arr[i], end = ' ')
  print()
    

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
